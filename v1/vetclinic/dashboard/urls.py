from django.urls import path
from .views import dashboard, owner_register, pet_register  # Import both views

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('register/owner/', owner_register, name='owner_register'),  # Owner registration
    path('register/pet/', pet_register, name='pet_register'),  # Pet registration
]
