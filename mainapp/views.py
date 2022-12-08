from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import get_user_model
User= get_user_model()
from .forms import CreateUserForm
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.

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