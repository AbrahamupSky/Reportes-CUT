# Generated by Django 4.2.6 on 2023-11-01 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Docentes', '0003_customuser_rol'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Reports', '0011_alter_reporte_docentes'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='jefe_departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='docentes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Docentes.customuser'),
        ),
    ]
