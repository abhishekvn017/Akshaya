# Generated by Django 5.0.3 on 2024-07-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('inspection_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_id', models.CharField(max_length=100)),
                ('inspection_date', models.DateField()),
                ('inspection_status', models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], max_length=20)),
                ('comments', models.TextField(blank=True, null=True)),
                ('inspected_by', models.CharField(max_length=100)),
                ('completed_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('unit_id', models.CharField(max_length=100)),
                ('maintenance_date', models.DateField()),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('maintenance_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('performed_by', models.CharField(max_length=100)),
                ('record_specifications', models.TextField()),
                ('comments', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PowerPlant',
            fields=[
                ('plant_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('capacity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_of_energy', models.CharField(choices=[('solar', 'Solar'), ('wind', 'Wind'), ('hydro', 'Hydro'), ('tidal', 'tidal')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=0)),
                ('action', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('contact_info', models.CharField(max_length=200)),
                ('designed_units', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_id', models.AutoField(primary_key=True, serialize=False)),
                ('plant_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('last_maintenance_date', models.DateField()),
                ('next_inspection_date', models.DateField()),
            ],
        ),
    ]