from django import forms
from django.forms import ModelForm

from Reports.admin import DocenteAdmin
from .models import Reporte

class ReportForm(ModelForm):
  class Meta:
    model = Reporte
    fields = ['titulo', 'academia', 'curso', 'ciclo', 'evidencia', 'turno', 'descripcion', 'docentes', 'archivo']

    widgets = {
      'titulo': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
      'academia': forms.Select(choices=Reporte.ACADEMY, attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'curso': forms.Select(choices=Reporte.CURSOS, attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'ciclo': forms.Select(choices=Reporte.CICLOS, attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'evidencia': forms.Select(choices=Reporte.EVIDENCIAS, attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'turno': forms.Select(choices=Reporte.TURNOS, attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'descripcion': forms.Textarea(attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500 resize-none', 'rows': 4}),
      'docentes': forms.Select(attrs={'class': 'px-4 w-full text-sm rounded-md focus:ring-blue-500 focus:border-blue-500 dark:placeholder-gray-400 dark:text-black dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'archivo': forms.ClearableFileInput(attrs={'class': 'sr-only', 'type': 'file'}),
    }
