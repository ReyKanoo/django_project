from django.urls import path, include
from . import views

urlpatterns = [
    path('/blocks', views.index, name='block'),
    path('create/', views.block_create, name='block_create'),
    path('', views.block_list, name='block_list'),
    path('<int:pk>/', views.block_detail, name='block_detail'),
    path('news/<pk>/', views.news, name='news'),
    path('<int:pk>/edit/', views.block_edit, name='block_edit'),
    path('<int:pk>/delete/', views.block_delete, name='block_delete')
]
