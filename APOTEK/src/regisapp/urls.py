from django.urls import path
from .views import register_view

app_name = 'regisapp'

urlpatterns = [
    path('', register_view, name='register'),
]
