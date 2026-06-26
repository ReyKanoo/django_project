from django.http import HttpResponse
from .models import block
from .forms import BlocksForm
from django.shortcuts import render, redirect

def index(request):
    # return HttpResponse("Главная страница")
    return render(request, 'blocks/index.html')




def block_list(request):
    return HttpResponse("Привет! Это список заданий")
    return render(request, 'blocks/block_list.html', {'blocks': blocks})
    
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
    block = block.objects.get(pk=pk)
    return render(request, 'blocks/block_detail.html', {'block': block, 'pk': pk})

def block_create(request):
    if request.method == 'POST':       # пользователь нажал кнопку
        form = BlocksForm(request.POST)
        if form.is_valid():             # данные прошли проверку
            form.save()                 # сохранить в БД
            return redirect('block_list')
    else:                              # пользователь открыл страницу
        form = BlocksForm()

    return render(request, 'blocks/block_create.html', {'form': form})


def block_edit(request, pk):
    block = block.objects.get(pk=pk)        # найти задание по pk

    if request.method == 'POST':
        form = BlocksForm(request.POST, instance=block)  # instance — говорим какой объект редактируем
        if form.is_valid():
            form.save()
            return redirect('block_list')
    else:
        form = BlocksForm(instance=block)    # форма уже заполнена данными задания

    return render(request, 'blocks/block_edit.html', {'form': form, 'block': block})


def block_delete(request, pk):
    block = block.objects.get(pk=pk)

    if request.method == 'POST':          # пользователь подтвердил удаление
        block.delete()
        return redirect('block_list')

    return render(request, 'blocks/block_delete.html', {'block': block})





