from django.urls import path
from . import views
from .views import ResepCreateView


app_name = 'uploadresepapp'

urlpatterns = [
    path('', ResepCreateView.as_view(), name='create'),
]
