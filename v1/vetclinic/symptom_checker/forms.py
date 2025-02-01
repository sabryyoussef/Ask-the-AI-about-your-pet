   # vetclinic/symptom_checker/forms.py
from django import forms
from .models import Symptom

class SymptomForm(forms.ModelForm):
       class Meta:
           model = Symptom
           fields = ['name', 'category', 'description', 'icon']