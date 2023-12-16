from django.shortcuts import render, redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.


# def add_album(request):
#     if request.method == 'POST':  # if user click submit button
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('add_album')

#     else:  # user normally website e gele blank form pabe
#         album_form = forms.AlbumForm()
#     return render(request, 'add_album.html', {'form': album_form})

class AddAlbumCreateView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('homepage')


# def edit_album(request, id):
#     album = models.Album.objects.get(pk=id)
#     album_form = forms.AlbumForm(instance=album)
#     if request.method == 'POST':  # if user click submit button
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('homepage')

#     return render(request, 'add_album.html', {'form': album_form})

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


# def delete_album(request, id):
#     album = models.Album.objects.get(pk=id)
#     album.delete()
#     return redirect('homepage')

class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')
