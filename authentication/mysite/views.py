from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created successfully!")
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            userPassword = form.cleaned_data['password']
            user = authenticate(username=name, password=userPassword)
            if user is not None:
                messages.success(request, "Logged In Successfully!")
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_profile(request):
    return render(request, 'profile.html')

# def user_profile(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ChangeUserData(request.POST, instance=request.user)
#             if form.is_valid():
#                 messages.success(request, 'Account updated successfully')
#                 form.save()
#         else:
#             form = ChangeUserData(instance=request.user)
#         return render(request, 'profile.html', {'form': form})
#     else:
#         return redirect('signup')


def user_logout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')


def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'form': form})
    else:
        return redirect('login')


def set_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'changepassword.html', {'form': form})
    else:
        return redirect('login')


def change_user_data(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save()
                print(form.cleaned_data)
                return redirect('profile')
        else:
            form = ChangeUserData(instance=request.user)
        return render(request, 'changeuserdata.html', {'form': form})
    else:
        return redirect('signup')
