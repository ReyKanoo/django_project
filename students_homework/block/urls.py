from django.urls import path, include

import views

urlpatterns = [
    path('/block', views.index, name='block')
]