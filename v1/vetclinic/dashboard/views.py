from django.shortcuts import render , render, redirect
from . forms import RegisterForm, OwnerRegistrationForm
from .forms import PetRegistrationForm



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'dashboard/register.html', {'form': form})


def owner_register(request):
    if request.method == "POST":
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            # Process owner registration (e.g., save to DB)
            return render(request, 'success.html')
    else:
        form = OwnerRegistrationForm()
    
    return render(request, 'owner_register.html', {'form': form})

def landing_page(request):
    return render(request, 'dashboard/landing_page.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')


def pet_register(request):
    if request.method == "POST":
        form = PetRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the data to the database if using a model
            # Pet.objects.create(**form.cleaned_data)
            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = PetRegistrationForm()
    
    return render(request, 'dashboard/pet_register.html', {'form': form})
