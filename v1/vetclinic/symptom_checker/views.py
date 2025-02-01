from django.shortcuts import render
from .models import Symptom

def symptom_checker(request):
    symptoms = Symptom.objects.all()  # Fetch all symptoms
    return render(request, 'symptom_checker/symptom_checker.html', {'symptoms': symptoms})

def symptom_list(request):
    symptoms = Symptom.objects.all()
    return render(request, 'symptom_list.html', {'symptoms': symptoms})
