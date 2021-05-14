from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
    path('index3', views.index3, name='index3'),
]