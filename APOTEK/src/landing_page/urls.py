from django.urls import path
from .views import LandingPageView  # hanya impor LandingPageView dari views
from . import views
app_name = 'landing_page'

urlpatterns = [
    # path('', views.landing_page, name='landing_page'),  # jika ingin menggunakan function-based view
    path('', LandingPageView.as_view(), name='landing_page'),
    path('beli/<int:obat_id>/', views.beli_obat, name='beli_obat'),
]

