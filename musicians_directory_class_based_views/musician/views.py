from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.


# def add_musician(request):
#     if request.method == 'POST':  # if user click submit button
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('add_musician')

#     else:  # user normally website e gele blank form pabe
#         musician_form = forms.MusicianForm()
#     return render(request, 'add_musician.html', {'form': musician_form})

class AddMusicianCreateView(CreateView):
    model = models.Musician
    template_name = 'add_musician.html'
    form_class = forms.MusicianForm
    success_url = reverse_lazy('add_musician')


# def edit_musician(request, id):
#     musician = models.Musician.objects.get(pk=id)
#     musician_form = forms.MusicianForm(instance=musician)
#     # print(post.title)
#     if request.method == 'POST':  # if user click submit button
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('homepage')

#     return render(request, 'add_musician.html', {'form': musician_form})

class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('homepage')
    pk_url_kwarg = 'id'
