from django.urls import path
from .views import homeuser_view

urlpatterns = [
    path('', homeuser_view, name='homeuser'),
]
