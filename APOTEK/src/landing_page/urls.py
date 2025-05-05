from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('beli/<int:obat_id>/', views.beli_obat, name='beli_obat'),
]
