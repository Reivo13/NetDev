from django.shortcuts import render


def home(request):
    items = range(10)  # Ini list angka dari 0-9
    return render(request, 'pages/landing_page.html', {'items': items})

