from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
# Create your views here.

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