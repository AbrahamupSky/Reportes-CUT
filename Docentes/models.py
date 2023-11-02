from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
  ROLES = (
    ('Jefe de Departamento', 'Jefe de Departamento'),
    ('Maestro', 'Maestro'),
    ('Presidente de Academia (Ingenieria de Software)', 'Presidente de Academia (Ingenieria de Software)'),
    ('Presidente de Academia (Programacion Avanzada)', 'Presidente de Academia (Programacion Avanzada)'),
    ('Presidente de Academia(Gestion de Datos)', 'Presidente de Academia(Gestion de Datos)'),
    ('Presidente de Academia(Gestion de Tecnologias)', 'Presidente de Academia(Gestion de Tecnologias)'),
  )
  
  codigoUDG = models.CharField(max_length=100)
  rol = models.CharField(max_length=100, choices=ROLES, default='Jefe de Departamento')

  # Especifica los related_name para evitar conflictos en los accesos inversos
  groups = models.ManyToManyField(
    Group,
    verbose_name=_('groups'),
    blank=True,
    help_text=_(
      'The groups this user belongs to. A user will get all permissions '
      'granted to each of their groups.'
    ),
    related_name='custom_user_groups',  # Nombre de acceso inverso único para CustomUser.groups
    related_query_name='user',
  )

  user_permissions = models.ManyToManyField(
    Permission,
    verbose_name=_('user permissions'),
    blank=True,
    help_text=_('Specific permissions for this user.'),
    related_name='custom_user_permissions',  # Nombre de acceso inverso único para CustomUser.user_permissions
    related_query_name='user',
  )

  def __str__(self):
    return self.username