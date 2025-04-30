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
    path('login/', include('loginapp.urls', namespace='loginapp')),
    path('register/', include('regisapp.urls', namespace='regisapp')),


    # Redirect dari URL utama (/) ke /homeuser/
    path('', lambda request: redirect('homeuser/')),  # Pengalihan ke halaman homeuser
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
