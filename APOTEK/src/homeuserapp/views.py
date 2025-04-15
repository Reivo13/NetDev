from django.shortcuts import render

def homeuser_view(request):
    return render(request, 'homeuserapp/homeuser.html')
