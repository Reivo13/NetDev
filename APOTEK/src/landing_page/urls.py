from django.urls import path
from .views import LandingPageView, beli_obat

urlpatterns = [
    path('beli/<int:obat_id>/', beli_obat, name='beli_obat'),
    path('', LandingPageView.as_view(), name='landing_page'),
]
