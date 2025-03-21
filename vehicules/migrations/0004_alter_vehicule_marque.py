from django.db import migrations, models
import django.db.models.deletion

def link_marques(apps, schema_editor):
    Vehicule = apps.get_model('vehicules', 'Vehicule')
    Marque = apps.get_model('vehicules', 'Marque')
    
    for vehicule in Vehicule.objects.all():
        marque = Marque.objects.get(nom=vehicule.marque)
        vehicule.marque_new = marque
        vehicule.save()

class Migration(migrations.Migration):
    dependencies = [
        ('vehicules', '0003_convert_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='marque_new',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='vehicules.marque'),
        ),
        migrations.RunPython(link_marques),
        migrations.RemoveField(
            model_name='vehicule',
            name='marque',
        ),
        migrations.RenameField(
            model_name='vehicule',
            old_name='marque_new',
            new_name='marque',
        ),
        migrations.AlterField(
            model_name='vehicule',
            name='marque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicules', to='vehicules.marque'),
        ),
    ] 