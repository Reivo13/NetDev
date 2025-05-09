# loginapp/urls.py
from django.urls import path
from .views import login_view, logout_view

app_name = 'loginapp'

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
