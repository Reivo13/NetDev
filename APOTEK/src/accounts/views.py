from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import RegisterForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    template_name = 'login.html'

def landing_page(request):
    return render(request, 'landing_page.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username sudah digunakan.')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email sudah digunakan.')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                messages.success(request, 'Registrasi berhasil! Silakan login.')
                return redirect('login')
        else:
            messages.error(request, 'Password tidak cocok.')
            return render(request, 'register.html')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Selamat datang, {user.username}!')

            # Redirect ke 'next' jika tersedia
            next_url = request.POST.get('next')
            return redirect(next_url) if next_url else redirect('landing_page')
        else:
            messages.error(request, 'Username atau password salah.')

    return render(request, 'login.html')

