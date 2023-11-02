from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Importa tu modelo de usuario personalizado

class CustomUserAdmin(UserAdmin):
  list_display = ['username', 'email', 'first_name', 'last_name', 'codigoUDG', 'rol', 'is_staff', 'is_superuser', 'date_joined']
  search_fields = ('username', 'email', 'first_name', 'last_name', 'codigoUDG', 'rol') 

# Registra tu modelo de usuario personalizado con el administrador personalizado
admin.site.register(CustomUser, CustomUserAdmin)
