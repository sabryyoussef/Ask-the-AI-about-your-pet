from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PetRegistrationForm(forms.Form):
    PET_CHOICES = [('Dog', 'Dog'), ('Cat', 'Cat')]
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    NEUTERED_CHOICES = [('Yes', 'Yes'), ('No', 'No')]
    WEIGHT_UNITS = [('Kg', 'Kg'), ('Lbs', 'Lbs')]

    pet_type = forms.ChoiceField(choices=PET_CHOICES, widget=forms.RadioSelect)
    pet_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your pet’s name'}))
    pet_breed = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Select or search your pet breed'}))
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2000, 2030)))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    neutered = forms.ChoiceField(choices=NEUTERED_CHOICES, widget=forms.RadioSelect)
    weight = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': '0'}))
    weight_unit = forms.ChoiceField(choices=WEIGHT_UNITS, widget=forms.Select)
    pet_photo = forms.ImageField(required=False)


class OwnerRegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
