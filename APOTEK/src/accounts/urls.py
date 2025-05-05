from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'  # Ubah dari 'login' ke 'accounts' untuk konsistensi

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        next_page='landing_page:landing_page'  # Redirect ke landing page setelah login
    ), name='login'),
    path('logout/', LogoutView.as_view(
        next_page='landing_page:landing_page'  # Redirect ke landing page setelah logout
    ), name='logout'),
    path('register/', views.register, name='register'),
    # Hapus duplikasi home/landing_page
]