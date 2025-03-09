from django.db import models
from django.core.validators import MinValueValidator

class Vehicule(models.Model):
    CATEGORIES = [
        ('CITADINE', 'Citadine'),
        ('BERLINE', 'Berline'),
        ('SUV', 'SUV'),
        ('UTILITAIRE', 'Utilitaire'),
        ('LUXE', 'Luxe'),
    ]

    nom = models.CharField(max_length=100)
    marque = models.CharField(max_length=50)
    modele = models.CharField(max_length=50)
    annee = models.IntegerField()
    categorie = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    prix_jour = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    disponible = models.BooleanField(default=True)
    image = models.ImageField(upload_to='vehicules/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Véhicule"
        verbose_name_plural = "Véhicules"
        ordering = ['-date_creation']

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"
