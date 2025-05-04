from django.urls import path
from . import views

app_name = 'resepapp'

urlpatterns = [
    path('', views.ResepListView.as_view(), name='list'),
    path('create/', views.ResepCreateView.as_view(), name='create'),
    path('<slug:slug>/', views.ResepDetailView.as_view(), name='detail'),
    path('<slug:slug>/edit/', views.ResepUpdateView.as_view(), name='update'),
]
