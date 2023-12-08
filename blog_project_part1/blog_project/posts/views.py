from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.


def add_post(request):
    if request.method == 'POST':  # user post request koreche
        # user er post request data ekhane capture korlam
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():  # post kora data gula amra valid kina check kortechi
            post_form.save()  # jodi data valid hoy taile database e save korbo
            # sob thik thakle take add author ei url e pathiye dibo
            return redirect('add_post')

    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    # print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')

    return render(request, 'add_post.html', {'form': post_form})


def delete_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
