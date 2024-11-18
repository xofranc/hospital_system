# Generated by Django 5.1.3 on 2024-11-14 03:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_rename_paciente_pacientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlergiaMedicamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.TextField()),
                ('tratamiento', models.TextField()),
                ('antecedentes_medicos', models.TextField(blank=True)),
                ('historial_enfermedades', models.TextField(blank=True)),
                ('observaciones', models.TextField(blank=True)),
                ('alergias', models.ManyToManyField(blank=True, to='historial.alergiamedicamento')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historias_atendidas', to='users.doctors')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias', to='users.pacientes')),
            ],
        ),
    ]