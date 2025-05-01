from django.urls import path
from .views import daftar_obat

urlpatterns = [
    path('', daftar_obat, name='daftar_obat'),
]