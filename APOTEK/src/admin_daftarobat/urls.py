from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='admin_daftarobat_index'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]