from django.http import HttpResponse
from .models import block
from .forms import BlockForm
from django.shortcuts import render, redirect



def task_create(request):
    if request.method == 'POST':       # пользователь нажал кнопку
        form = BlockForm(request.POST)
        if form.is_valid():             # данные прошли проверку
            form.save()                 # сохранить в БД
            return redirect('block_list')
    else:                              # пользователь открыл страницу
        form = BlockForm()

    return render(request, 'block/block_create.html', {'form': form})








