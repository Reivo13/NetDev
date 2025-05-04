# your_app/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = "riwayat"
urlpatterns = [
    path('', views.riwayat, name='riwayat'),
    # tambahkan path lain seperti resep_obat, login jika ada
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)