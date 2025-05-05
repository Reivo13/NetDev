# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
app_name = 'login'


urlpatterns = [
    path('', views.home, name='landing_page'), 
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', views.home, name='home'),
]
