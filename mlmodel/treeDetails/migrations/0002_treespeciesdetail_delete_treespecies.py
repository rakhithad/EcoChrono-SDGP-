# Generated by Django 5.0.1 on 2024-03-09 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeDetails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreeSpeciesDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specie_name', models.CharField(max_length=20)),
                ('specie_info', models.TextField()),
                ('specie_growth_factor', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.DeleteModel(
            name='TreeSpecies',
        ),
    ]
