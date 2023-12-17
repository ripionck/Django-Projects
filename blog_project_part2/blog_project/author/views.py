from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
# Create your views here.


# def add_author(request):
#     if request.method == 'POST':
#         author_form = forms.AuthorForm(request.POST)
#         if author_form.is_valid():
#             author_form.save()
#             return redirect('add_author')

#     else:
#         author_form = forms.AuthorForm()
#     return render(request, 'add_author.html', {'form': author_form})

def register(request):
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('user_login')
            messages.success(request, 'Account created successfully!')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'Register'})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in successfully!')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Your informatiom is incorrect!')
                return redirect('register')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form': form, 'type': 'Login'})


@login_required
def profile(request):
    data = Post.objects.filter(author=request.user)
    return render(request, 'profile.html', {'data': data})


@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')

    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': profile_form})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password changed successfully!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('user_login')
