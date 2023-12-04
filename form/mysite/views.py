from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def hmtl_form(request):
    return render(request, 'html_form.html')


def django_form(request):
    return render(request, 'django_form.html')
