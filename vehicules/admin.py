from django.contrib import admin
from .models import Vehicule, Marque

@admin.register(Marque)
class MarqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_creation')
    search_fields = ('nom',)
    ordering = ('nom',)

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'marque', 'modele', 'categorie', 'prix_jour', 'disponible')
    list_filter = ('categorie', 'disponible', 'marque')
    search_fields = ('nom', 'modele')
    ordering = ('-date_creation',)
