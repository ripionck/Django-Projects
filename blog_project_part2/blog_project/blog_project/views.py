from django.shortcuts import render
from posts.models import Post
from categories.models import Category


def homepage(request, category_slug=None):  # initially dhore nicchi je category_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile category te click korlei sei category er slug ta capture korbo ar seta tokhn ar None thakbe na
    data = Post.objects.all()  # sob post gula ke niye aslam
    if category_slug is not None:  # ekhn category slug jodi None na hoy tar mane sekhane value ache
        # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug sei category object peye jabo
        category = Category.objects.get(slug=category_slug)
        # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
        data = Post.objects.filter(category=category)
    categories = Category.objects.all()  # sob category dekhabo
    return render(request, 'home.html', {'data': data, 'categories': categories})
