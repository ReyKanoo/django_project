from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required

from .models import block
from .forms import BlocksForm

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'blocks/index.html')



@login_required
def block_list(request):
    # return HttpResponse("Привет! Это список блокировок")
    blocks = block.objects.all()

    if Profile.role == 'editor':
        blocks = block.objects.all()       # преподаватель видит всё
    else:
        blocks = block.objects.filter(author=request.user)  # ученик только своё

    paginator = Paginator(blocks, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blocks/block_list.html', {'page_obj': page_obj})
    

def news(request, pk):
    return HttpResponse(f"Проверка страница {pk}")


def block_detail(request, pk):
    # blocks = [
    #     {'title': 'Сделать уроки',    'description': 'Математика и русский'},
    #     {'title': 'Прочитать книгу',  'description': 'Глава 3 и 4'},
    #     {'title': 'Написать код',    'description': 'Django проект'},
    # ]
    # block = blocks[pk - 1]   # pk с 1, список с 0
    # return render(request, 'blocks/block_detail.html', {'block': block, 'pk': pk})
    blocks = block.objects.get(pk=pk)
    return render(request, 'blocks/block_detail.html', {'item': blocks, 'pk': pk})

@login_required
def block_create( request): 
    if request.method == 'POST':       
        form = BlocksForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)   
            task.author = request.user              
            form.save()                 
            return redirect('block_list')
    else:                              
        form = BlocksForm()

    return render(request, 'blocks/block_create.html', {'form': form})


def block_edit(request, pk):
    blocks = block.objects.get(pk=pk)        # найти задание по pk

    if request.method == 'POST':
        form = BlocksForm(request.POST, instance=blocks)  # instance — говорим какой объект редактируем
        if form.is_valid():
            form.save()
            return redirect('block_list')
    else:
        form = BlocksForm(instance=blocks)    # форма уже заполнена данными задания

    return render(request, 'blocks/block_edit.html', {'form': form, 'block': blocks})

@login_required
def block_delete(request, pk):
    blocks = block.objects.get(pk=pk)

    if request.user.profile.role != 'editor':
        return redirect('task_list')     

    if request.method == 'POST':          # пользователь подтвердил удаление
        blocks.delete()
        return redirect('block_list')

    return render(request, 'blocks/block_delete.html', {'blocks': blocks})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            Profile.objects.create(
                user=user,
                role=form.cleaned_data['role']
            )
            login(request, user)
            return redirect('block_list')
    else:
        form = RegisterForm()
    return render(request, 'blocks/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('block_list')
    else:
        form = LoginForm()
    return render(request, 'blocks/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('user_login')