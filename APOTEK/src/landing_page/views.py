from django.shortcuts import render


def landing_page(request):
    items = range(10)  # Ini list angka dari 0-9
    return render(request, 'pages/landing_page.html', {'items': items})

