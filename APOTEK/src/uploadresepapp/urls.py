from django.urls import path
from . import views

app_name = 'uploadresepapp'

urlpatterns = [
    path('upload/', views.upload_resep, name='upload'),
    path('daftar/', views.daftar_resep, name='daftar'),
]
