from django.shortcuts import render , render, redirect
from . forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'dashboard/register.html', {'form': form})

def landing_page(request):
    return render(request, 'dashboard/landing_page.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')