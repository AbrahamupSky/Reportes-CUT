from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import CustomUser  # Asegúrate de importar tu modelo de usuario personalizado

class CustomUserAdmin(UserAdmin):
  list_display = ['username', 'email', 'first_name', 'last_name', 'codigoUDG', 'rol', 'is_staff', 'is_superuser', 'date_joined']
  search_fields = ('username', 'email', 'first_name', 'last_name', 'codigoUDG', 'rol') 

  def get_actions(self, request):
    # Deshabilitar la acción de eliminación para usuarios superusuarios
    actions = super().get_actions(request)
    if 'delete_selected' in actions and request.user.is_superuser:
      del actions['delete_selected']
    return actions

# Registra tu modelo de usuario personalizado con el administrador personalizado
admin.site.register(CustomUser, CustomUserAdmin)
