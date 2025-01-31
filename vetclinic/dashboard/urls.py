from django.urls import path
from .views import register
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
]