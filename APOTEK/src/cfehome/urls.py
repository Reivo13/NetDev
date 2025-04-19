from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeuser/', include('homeuserapp.urls')),  # Mengarahkan ke app homeuser
    path('adminapp/', include('adminapp.urls', namespace="adminapp")),
    path('resepapp/', include('resepapp.urls', namespace="resepapp")),
    path('obat/', include('daftarobat.urls')),
    
    # Redirect dari URL utama (/) ke /homeuser/
    path('', lambda request: redirect('homeuser/')),  # Pengalihan ke halaman homeuser
    path('history/', include('history.urls', namespace='history')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
