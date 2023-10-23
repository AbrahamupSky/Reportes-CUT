from django import forms
from django.forms import ModelForm

from Reports.admin import DocenteAdmin
from .models import Reporte

class ReportForm(ModelForm):
  class Meta:
    model = Reporte
    fields = ['titulo', 'academia', 'curso', 'ciclo', 'evidencia', 'turno', 'descripcion', 'docentes']#, 'archivo']

    widgets = {
      'titulo': forms.TextInput(attrs={'class': 'h-10 border mt-1 rounded px-4 w-full bg-gray-50'}),
      'academia': forms.Select(choices=Reporte.ACADEMY, attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
      'curso': forms.Select(choices=Reporte.CURSOS, attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
      'ciclo': forms.Select(choices=Reporte.CICLOS, attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
      'evidencia': forms.Select(choices=Reporte.EVIDENCIAS, attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
      'turno': forms.Select(choices=Reporte.TURNOS, attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
      'descripcion': forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
      'docentes': forms.Select(attrs={'class': 'px-4 appearance-none outline-none text-gray-800 w-full bg-transparent'}),
    }
