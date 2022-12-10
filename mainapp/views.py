from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import User

from .forms import CreateUserForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt 
def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = CreateUserForm()

    context = {'form':form}
    return render(request, 'mainapp/signup.html', context)


def frontpage(request):
    return render(request, 'mainapp/frontpage.html')

def login(request):
    context = {}
    return render(request, 'mainapp/login.html', context)

@csrf_exempt 
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()



    context = {'form':form}
    return render(request, 'mainapp/register.html', context)