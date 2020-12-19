from django.shortcuts import render, redirect
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm)
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please login here.')
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
