from django.urls import path, include

from . import views
# from blocks import views

urlpatterns = [
    path('', views.index, name='index'),
]