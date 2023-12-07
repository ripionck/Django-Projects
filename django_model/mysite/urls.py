from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:roll>', views.delete_student, name='delete_student'),
    path('add_student/', views.add_student, name='add_student')
]
