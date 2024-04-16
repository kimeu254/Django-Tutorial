from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from account.forms import RegisterForm, LoginForm, ProfileForm
from django.http import *

def register_user(request):

    context = {}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['form'] = form
    else:
        form = RegisterForm()
        context['form'] = form

    return render(request, 'account/register.html', context)

def login_user(request):

    context = {}

    user = request.user

    if user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()

    context['form'] = form
    return render(request, 'account/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')

def account_user(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['form'] = form
    context['success_message'] = "Profile Saved Successfully!"
    return render(request, 'account/profile.html', context)