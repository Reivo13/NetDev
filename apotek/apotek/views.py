from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("Ini halaman register!")

def login_view(request):
    return HttpResponse("Ini halaman login!")
