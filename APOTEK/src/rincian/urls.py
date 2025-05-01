from django.urls import path
from . import views

urlpatterns = [
    path('rincian/', views.rincian, name='rincian'),
    
]
