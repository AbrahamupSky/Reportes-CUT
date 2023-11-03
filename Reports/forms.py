from django import forms
from django.forms import ModelForm

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
      'archivo': forms.FileInput(attrs={'class': 'cursor-pointer block w-full border border-gray-200 shadow-sm rounded-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:border-gray-700 dark:text-gray-400 file:border-0 file:bg-gray-100 file:mr-4 file:py-2 file:px-4 dark:file:text-gray-400', 'type': 'file', 'id': 'file_input'}),
    }
