from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework import status
from .models import Projects,Review
from rest_framework import viewsets

def register(request):
    if request.user.is_authenticated:
        return redirect('base')
    else:
        form = CreateUserForm()
        if request.method=='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                return redirect('base')
    return render(request,'users/register.html',{'form':form})


def produse(request):
    produs = Projects.objects.all()
    context = {'produs':produs}
    return render(request,'produse.html',context)


def test(request):
    produs = Projects.objects.all()

    context = {'produs':produs}
    return render(request,'test.html',context)

def produs(request,pk):
    p = Projects.objects.get(id=pk)
    rew = p.Review.all()
    return render(request,'produs.html',{'produs':rew})

def base(request):
    return render(request,'base.html')

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('base')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('base')
    return render(request,'users/login.html')

login_required(login_url='loginuser')
def logoutuser(request):
    logout(request)
    return redirect('base')


def account(request):
     
     email =request.user.email
     username  = request.user
     name = request.user.first_name
     secondname = request.user.last_name
     return render(request,'users/account.html',{'email':email,'username':username,'name':name,'second':secondname})



