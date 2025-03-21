from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ('vehicules', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='marques/')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
    ] 