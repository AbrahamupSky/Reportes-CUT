# Generated by Django 4.2.6 on 2023-10-23 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0004_remove_reporte_archivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reporte',
            name='docentes',
        ),
        migrations.AddField(
            model_name='reporte',
            name='docentes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Reports.docente'),
        ),
    ]
