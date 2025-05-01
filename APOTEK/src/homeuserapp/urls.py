from django.urls import path
from .views import homeuser_view

app_name = 'homeuserapp'

urlpatterns = [
    path('', homeuser_view, name='homeuser'),
]
