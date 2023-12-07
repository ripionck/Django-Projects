from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('html_form/', views.hmtl_form, name='html_form'),
    # path('django_form/', views.django_form, name='django_form'),
    # path('django_form/', views.StudentForm, name='django_form'),
    path('django_form/', views.PasswordValidation, name='django_form'),
]
