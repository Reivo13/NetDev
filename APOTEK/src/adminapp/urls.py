from django.urls import path
from .views import (
    DataObatListView,
    DataObatDetailView,
    DataObatCreateView,
    DataObatUpdateView
)

app_name = 'adminapp'

urlpatterns = [
    path('', DataObatListView.as_view(), name='list'),
    path('create/', DataObatCreateView.as_view(), name='create'),
    path('<slug:slug>/', DataObatUpdateView.as_view(), name='detail'),
    #path('<slug:slug>/edit/', DataObatUpdateView.as_view(), name='update'),
]