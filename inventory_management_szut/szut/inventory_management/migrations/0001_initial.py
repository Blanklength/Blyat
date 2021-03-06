# Generated by Django 4.0.5 on 2022-06-16 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gerat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('kosten', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Kosten')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'beschränkt funktionsfähig'), (5, 'funktionsfähig'), (0, 'funktionsunfähig')], null=True, verbose_name='Status')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Beschreibung')),
                ('bestellungs_datum', models.DateField(blank=True, null=True, verbose_name='Bestellungsdatum')),
                ('serien_nummer', models.CharField(blank=True, max_length=40, null=True, verbose_name='Seriennummer')),
                ('garantie_monate', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11)], null=True, verbose_name='Garantie (Monate)')),
                ('garantie_jahre', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19)], null=True, verbose_name='Garantie (Jahre)')),
            ],
            options={
                'verbose_name': 'Gerät',
                'verbose_name_plural': 'Geräte',
            },
        ),
        migrations.CreateModel(
            name='Geratehersteller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Gerätehersteller',
                'verbose_name_plural': 'Gerätehersteller',
            },
        ),
        migrations.CreateModel(
            name='Geratekategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Gerätekategorie',
                'verbose_name_plural': 'Gerätekategorien',
            },
        ),
        migrations.CreateModel(
            name='Stockwerk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Stockwerk',
                'verbose_name_plural': 'Stockwerke',
            },
        ),
        migrations.CreateModel(
            name='Trakt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Trakt',
                'verbose_name_plural': 'Trakte',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=40, verbose_name='Titel')),
                ('description', models.TextField(max_length=500, verbose_name='Beschreibung')),
                ('status', models.IntegerField(choices=[(1, 'Offen'), (0, 'Erledigt')], verbose_name='Status')),
                ('erstellungs_datum', models.DateTimeField(auto_now_add=True, verbose_name='Erstellungsdatum')),
                ('gerat', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.gerat', verbose_name='Gerät')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.CreateModel(
            name='Raum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('building_section', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='inventory_management.trakt', verbose_name='Bauabschnitt')),
                ('floor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='inventory_management.stockwerk', verbose_name='Etage')),
            ],
            options={
                'verbose_name': 'Raum',
                'verbose_name_plural': 'Räume',
            },
        ),
        migrations.AddField(
            model_name='gerat',
            name='gerate_hersteller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.geratehersteller', verbose_name='Hersteller'),
        ),
        migrations.AddField(
            model_name='gerat',
            name='gerate_kategorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.geratekategorie', verbose_name='Kategorie'),
        ),
        migrations.AddField(
            model_name='gerat',
            name='raum',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventory_management.raum', verbose_name='Raum'),
        ),
    ]
