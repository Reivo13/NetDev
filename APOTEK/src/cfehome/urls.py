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
    path('homeuser/', include('homeuserapp.urls')),
    path('admin_resep/', include('admin_resep.urls')),
    path('adminapp/', include('adminapp.urls', namespace="adminapp")),
    path('resepapp/', include('resepapp.urls', namespace="resepapp")),
    path('obat/', include('daftarobat.urls')),
    path('history/', include('history.urls', namespace='history')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('', lambda request: redirect('homeuser/')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)