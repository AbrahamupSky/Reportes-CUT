# Generated by Django 4.2.6 on 2023-11-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docentes', '0003_customuser_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='rol',
            field=models.CharField(choices=[('Jefe de Departamento', 'Jefe de Departamento'), ('Administrador', 'Administrador'), ('Operador', 'Operador'), ('Técnico', 'Técnico')], default='Jefe de Departamento', max_length=100),
        ),
    ]