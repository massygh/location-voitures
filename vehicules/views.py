from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Vehicule

# Create your views here.

def home(request):
    vehicules = Vehicule.objects.filter(disponible=True)[:6]  # Affiche les 6 derniers véhicules disponibles
    return render(request, 'vehicules/home.html', {'vehicules': vehicules})

def location(request):
    return render(request, 'vehicules/location.html')

@login_required
def profile(request):
    return render(request, 'vehicules/profile.html')

@login_required
def mes_locations(request):
    return render(request, 'vehicules/mes_locations.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('vehicules:home')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'vehicules/login.html')

def logout_view(request):
    logout(request)
    return redirect('vehicules:home')

def register(request):
    return render(request, 'vehicules/register.html')
