from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def start(request):
    title = 'Welcome!'
    context = {'title': title}
    return render(request, 'firstPage.html', context)


def login(request):
    title = 'Login!'
    context = {'title': title}
    return render(request, 'login.html', context)


def forgot(request):
    title = 'Forgot Password!'
    context = {'title': title}
    return render(request, 'forgot.html', context)