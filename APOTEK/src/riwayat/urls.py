# your_app/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import RiwayatPembelianView

app_name = 'riwayat'

urlpatterns = [
    path('', RiwayatPembelianView.as_view(), name='riwayat_pembelian'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)