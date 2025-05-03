from django.urls import path
from .views import homeuser_view
from django.contrib.auth.views import LoginView


app_name = 'homeuserapp'
urlpatterns = [
    path('', homeuser_view, name='homeuser'),
]
