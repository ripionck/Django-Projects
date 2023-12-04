from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('html_form/', views.hmtl_form, name='html_form'),
    path('django_form/', views.django_form, name='django_form')
]
