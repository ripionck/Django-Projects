from django.shortcuts import render

# Create your views here.


def index(request):

    d = {'author': 'Anjela Yu', 'age': 35, 'list': [
        'mango', 'banana', 'apple', 'orange', 'lichi']}

    return render(request, 'index.html', d)
