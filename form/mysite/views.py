from django.shortcuts import render
from . forms import contactForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name': name, 'email': email})
    else:
        return render(request, 'about.html')


def hmtl_form(request):
    return render(request, 'html_form.html')


def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(request, 'django_form.html', {'form': form})
