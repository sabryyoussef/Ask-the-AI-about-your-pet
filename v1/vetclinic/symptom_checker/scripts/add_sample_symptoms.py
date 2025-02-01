from vetclinic.symptom_checker.models import Symptom

def add_sample_symptoms():
    sample_symptoms = [
        {"name": "Coughing", "category": "breathing", "description": "Persistent cough"},
        {"name": "Limping", "category": "mobility", "description": "Difficulty walking"},
        {"name": "Itchy Skin", "category": "skin_coat", "description": "Frequent scratching"},
    ]

    for symptom_data in sample_symptoms:
        Symptom.objects.create(**symptom_data)

if __name__ == "__main__":
    add_sample_symptoms() 