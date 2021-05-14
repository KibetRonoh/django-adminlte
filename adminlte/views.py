from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def login(request):
    return render(request, 'accounts/login.html')


def register(request):
    return render(request, 'adminlte/register.html')


@login_required(login_url='accounts/login/')
def index1(request):
    return render(request, 'adminlte/index1.html')


def index2(request):
    return render(request, 'adminlte/index2.html')


def index3(request):
    return render(request, 'adminlte/index3.html')