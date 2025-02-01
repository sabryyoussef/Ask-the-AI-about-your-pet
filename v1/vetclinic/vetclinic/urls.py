"""
URL configuration for vetclinic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from dashboard import views
from dashboard.views import pet_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.landing_page, name='landing_page'),
    path('odoo/', include('odoo_integration.urls')),
    path('ai/', include('ai_integration.urls')),
    path('symptom_checker/', include(('symptom_checker.urls', 'symptom_checker'), namespace='symptom_checker')),
    path('register/', views.register, name='register'),
    path('register/pet', pet_register, name='pet_register'),
]
