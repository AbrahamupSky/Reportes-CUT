import io
import csv
import time
import calendar

from io import BytesIO
from .models import Reporte
from datetime import datetime
from .forms import ReportForm
from calendar import HTMLCalendar
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, FileResponse

# ? Pagina para generar reporte general
@login_required(login_url='login')
def general_report(request):
  return render(request, 'reports/general_report.html')

# ! Eliminar reporte
@login_required(login_url='login')
def delete_report(request, report_id):
  report = Reporte.objects.get(pk=report_id)
  report.delete()
  time.sleep(.5)
  return redirect('specific_reports')

# ? Subir reportes
@login_required(login_url='login')
def upload_docs(request):
  submitted = False
  if request.method == 'POST':
    form = ReportForm(request.POST)
    if form.is_valid():
      report = form.save(commit=False)
      report.docentes = request.user
      form.save()
      time.sleep(1.5)
      return HttpResponseRedirect('/upload?submitted=True')
  else:
    form = ReportForm()

  if 'submitted' in request.GET:
    submitted = True

  else:
    error_message = "Por favor, asegúrate de llenar todos los campos del formulario."
    return render(request, 'reports/upload_docs.html', {
      'form': form,
      'error_message': error_message,
    })

  return render(request, 'reports/upload_docs.html', {
    'form': form,
    'submitted': submitted,
  })

# ? Mostrar 1 solo reporte
@login_required(login_url='login')
def show_report(request, report_id):
  report = Reporte.objects.get(pk=report_id)
  form = ReportForm(request.POST or None, instance=report)
  if form.is_valid():
    form.save()
    time.sleep(1.5)
    return redirect('specific_reports')

  return render(request, 'reports/show_report.html', {
    'report': report,
    'form': form,
  })

# ? Mostrar todos los reportes
@login_required(login_url='login')
def all_reports(request):
  report_list = Reporte.objects.all()

  return render(request, 'reports/general_report.html', {
    'report_list': report_list,
  })

# ? Mostrar todos los reportes de un solo maestro
@login_required(login_url='login')
def specific_reports(request):
  # report_list = Reporte.objects.all()
  logged_user = request.user
  reports = Reporte.objects.filter(docentes=logged_user)

  return render(request, 'reports/report_list.html', {
    'reports': reports,
  })

# ? Mostrar página de inicio donde estan los menu
@login_required(login_url='login')
def inicio(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
  name = 'Abraham'
  month = month.title()
  # ? Convert Month to number
  month_number = list(calendar.month_name).index(month)
  month_number = int(month_number)

  # ? Create a calendar
  cal = HTMLCalendar().formatmonth(year, month_number)

  # ? Get current year
  now = datetime.now()
  current_year = now.year

  # ? Get current time
  time = now.strftime("%I:%M %p")

  return render(request, 'reports/home.html', {
    'name': name,
    'year': year,
    'month': month,
    'month_number': month_number,
    'cal': cal,
    'current_year': current_year,
    'time': time,
  })

# ? Pagina de about
def about(request):
  return render(request, 'about.html')