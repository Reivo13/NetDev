from django.urls import path
from .views import (
    DataObatListView,
    DataObatDetailView,
    DataObatCreateView,
    DataObatUpdateView,
    DataObatDeleteView,
    DashboardView,
)
app_name = 'adminapp'

urlpatterns = [
    path('', DashboardView.as_view(), name='list'),
    path('create/', DataObatCreateView.as_view(), name='create'),
    path('<slug:slug>/', DataObatDetailView.as_view(), name='detail'),  # untuk halaman detail (opsional)
    path('<slug:slug>/update/', DataObatUpdateView.as_view(), name='update'),  # ✅ ini penting untuk update
    path('<slug:slug>/delete/', DataObatDeleteView.as_view(), name='delete'),
]
