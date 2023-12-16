from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('set_password/', views.set_password, name='set_password'),
    path('change_user_data/', views.change_user_data, name='change_user_data'),
]
