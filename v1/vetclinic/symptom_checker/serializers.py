   # vetclinic/symptom_checker/serializers.py
from rest_framework import serializers
from .models import Symptom

class SymptomSerializer(serializers.ModelSerializer):
       class Meta:
           model = Symptom
           fields = ['id', 'name', 'category', 'description', 'icon']