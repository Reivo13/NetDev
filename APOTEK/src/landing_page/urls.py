from django.urls import path
from .views import LandingPageView
from . import views  # atau impor spesifik fungsi beli_obat

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path('beli/<int:obat_id>/', views.beli_obat, name='beli_obat'),
]