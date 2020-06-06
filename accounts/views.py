from django.shortcuts import render, redirect
from .forms import CustomCreation, LoginForm
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('accounts:index')
    return render(request, 'accounts/login.html', {'form':form})


def register_view(request):
    form = CustomCreation(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        
        return redirect('accounts:index')
    return render(request, 'accounts/register.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('accounts:index')