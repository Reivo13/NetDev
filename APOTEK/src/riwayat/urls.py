# your_app/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.riwayat, name='riwayat'),
    path('faq/', views.faq, name='faq'),
    path('syarat/', views.syarat, name='syarat'),
    path('kebijakan/', views.kebijakan, name='kebijakan'),
    # tambahkan path lain seperti resep_obat, login jika ada
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)