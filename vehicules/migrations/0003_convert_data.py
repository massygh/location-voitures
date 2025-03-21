from django.db import migrations

def convert_marques(apps, schema_editor):
    Vehicule = apps.get_model('vehicules', 'Vehicule')
    Marque = apps.get_model('vehicules', 'Marque')
    
    # Crée d'abord toutes les marques uniques
    marques_existantes = set(Vehicule.objects.values_list('marque', flat=True))
    for nom_marque in marques_existantes:
        Marque.objects.get_or_create(nom=nom_marque)

class Migration(migrations.Migration):
    dependencies = [
        ('vehicules', '0002_create_marque'),
    ]

    operations = [
        migrations.RunPython(convert_marques),
    ] 