from django.shortcuts import render
from django.http import HttpResponseRedirect
import calendar
import time
from calendar import HTMLCalendar
from datetime import datetime
from .models import Docente, Reporte
from .forms import ReportForm

def upload_docs(request):
  submitted = False
  if request.method == 'POST':
    form = ReportForm(request.POST)
    if form.is_valid():
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

def show_report(request, report_id):
  report = Reporte.objects.get(pk=report_id)
  form = ReportForm(request.POST or None)

  return render(request, 'reports/show_report.html', {
    'report': report,
    'form': form,
  })

def all_reports(request):
  report_list = Reporte.objects.all()

  return render(request, 'reports/report_list.html', {
    'report_list': report_list,
  })

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

def about(request):
  return render(request, 'about.html')