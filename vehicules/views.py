from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Vehicule, Marque

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

def vehicules(request):
    return vehicules_list(request)

def vehicule_detail(request, vehicule_id):
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)
    return render(request, 'vehicules/vehicule_detail.html', {'vehicule': vehicule})

def vehicules_list(request):
    vehicules = Vehicule.objects.all()
    marques = Marque.objects.all()
    
    # Filtres
    marque_ids = request.GET.getlist('marque')
    prix_max = request.GET.get('prix_max')
    categorie = request.GET.get('categorie')
    tri = request.GET.get('tri', 'recent')
    
    # Convertir les IDs en entiers pour la comparaison dans le template
    selected_marques = [int(m_id) for m_id in marque_ids if m_id.isdigit()]
    
    if marque_ids:
        vehicules = vehicules.filter(marque_id__in=marque_ids)
    if prix_max:
        vehicules = vehicules.filter(prix_jour__lte=prix_max)
    if categorie:
        vehicules = vehicules.filter(categorie=categorie)
    
    # Tri
    if tri == 'prix_croissant':
        vehicules = vehicules.order_by('prix_jour')
    elif tri == 'prix_decroissant':
        vehicules = vehicules.order_by('-prix_jour')
    elif tri == 'recent':
        vehicules = vehicules.order_by('-date_creation')
    
    context = {
        'vehicules': vehicules,
        'marques': marques,
        'selected_marques': selected_marques,
        'tri_actuel': tri
    }
    return render(request, 'vehicules/vehicules.html', context)
