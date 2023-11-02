from .models import Reporte
from django.contrib import admin

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'academia', 'curso', 'ciclo', 'evidencia', 'turno', 'fecha', 'descripcion']#, 'archivo'
  ordering = ('-fecha', )
  search_fields = ('titulo', 'academia', 'curso', 'docentes')