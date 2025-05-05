from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from accounts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('homeuser/', include('homeuserapp.urls', namespace="homeuserapp")),
    path('admin_resep/', include('admin_resep.urls')),
    path('admin_daftarobat/', include('admin_daftarobat.urls')),
    path('admin_tambahobat/', include('admin_tambahobat.urls')),
    path('adminapp/', include('adminapp.urls', namespace="adminapp")),
    path('resepapp/', include('resepapp.urls', namespace="resepapp")),
    path('obat/', include('daftarobat.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logindjanggo/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('uploadresep/',include('uploadresepapp.urls'), name='uploadresepapp'),
    path('riwayat/',include('riwayat.urls'), name='riwayat'),
    #path('', lambda request: redirect('homeuser/')),
    path('', include('landing_page.urls')),
    path('login/', include('loginapp.urls', namespace='loginapp')),
    path('regist/', include('regisapp.urls', namespace='regisapp')),


    # Redirect dari URL utama (/) ke /homeuser/
    path('', lambda request: redirect('homeuser/')),  # Pengalihan ke halaman homeuser
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
