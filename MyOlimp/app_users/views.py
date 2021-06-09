from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm, UserRegisterForm
from .models import *


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = '/users/login'


def password_change_view(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(date=request.POST, user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            return redirect('users/login')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'password_form': pass_form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/users/login')
    else:
        user_form = UserRegisterForm()
    return render(request, 'users/create_user.html', {'user_form': user_form})

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
        else:
            profile_form.add_error('__all__', 'Данные введены неверно!')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
        })
