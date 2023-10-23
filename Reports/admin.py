from django.contrib import admin
from .models import Docente, Reporte

# admin.site.register(Docente)
# admin.site.register(Reporte)

@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
  list_display = ['titulo', 'academia', 'curso', 'ciclo', 'evidencia', 'turno', 'fecha', 'descripcion']#, 'archivo'
  ordering = ('-fecha', )
  search_fields = ('titulo', 'academia', 'curso', 'docentes')

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
  list_display = ['codigoUDG', 'nombres', 'apellidos', 'email']
  search_fields = ('codigoUDG', 'nombres', 'apellidos', 'email')
  list_filter = ('codigoUDG', 'nombres', 'apellidos')
  ordering = ('-codigoUDG', )