from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                # Always redirect to root URL '/' after login for normal users
                if user.is_superuser:
                    return redirect('adminapp:list')
                else:
                    return redirect('/')
            else:
                form.add_error(None, 'Username atau password salah')
    else:
        form = LoginForm()
    return render(request, 'loginapp/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/')
