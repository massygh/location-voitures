from django.contrib import admin
from .models import Vehicule

@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'marque', 'modele', 'categorie', 'prix_jour', 'disponible')
    list_filter = ('categorie', 'disponible', 'marque')
    search_fields = ('nom', 'marque', 'modele')
    ordering = ('-date_creation',)
