# vetclinic/symptom_checker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.symptom_checker, name='symptom_checker'),  # Root path for the app
]