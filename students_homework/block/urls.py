from django.urls import path, include
# from views import block_create
from . import views

urlpatterns = [
    path('/block', views.index, name='block')
]