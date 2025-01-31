# odoo_integration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.odoo_login, name='odoo_login'),
]