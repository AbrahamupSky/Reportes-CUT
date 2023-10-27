import io
import csv
import time
import calendar
from fpdf import FPDF
from io import BytesIO
from .models import Reporte, Docente
from datetime import datetime
from .forms import ReportForm
from calendar import HTMLCalendar
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, FileResponse

# ? Pagina para generar reporte general
def general_report(request):
  return render(request, 'reports/general_report.html')

# ? Generar archivo PDF
def pdf_report(request):
  pdf = FPDF(orientation='L', unit='mm', format='A4')
  pdf.add_page()

  # ? Asignar el modelo
  reports = Docente.objects.all()

  for docente in reports:
    pdf.set_font('helvetica', 'B', 14)
    pdf.set_text_color(255)

    # ? Codigo UDG del Docente
    pdf.cell(w=40, h=15, txt='Codigo UDG', border=1, align='C', fill=True)
    pdf.set_text_color(0)
    pdf.multi_cell(w=120, h=15, txt=str(docente.codigoUDG), border=1, align='C', fill=0)

    # ? Nombre Docente
    pdf.set_text_color(255)
    pdf.cell(w=40, h=15, txt='Nombre', border=1, align='C', fill=True)
    pdf.set_text_color(0)
    pdf.multi_cell(w=120, h=15, txt=f"{docente.nombres} {docente.apellidos}", border=1, align='C', fill=0)

    # ? Correo Docente
    pdf.set_text_color(255)
    pdf.cell(w=40, h=15, txt='Correo', border=1, align='C', fill=True)
    pdf.set_text_color(0)
    pdf.multi_cell(w=120, h=15, txt=str(docente.email), border=1, align='C', fill=0)

    pdf.image('static/media/cut.png', 210, 7, 50, 50)

    # ? Titulo tabla
    pdf.ln(10)
    pdf.set_fill_color(29, 29, 29)
    pdf.set_text_color(255)
    pdf.cell(w=0, h=10, txt="Reporte de Actividades", border=1, ln=1, align='C', fill=True)

    # ? Tabla datos
    pdf.set_fill_color(50, 50, 50)
    pdf.set_text_color(255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(w=10, h=8, txt='#', border=1, align='C', fill=True)
    pdf.cell(w=40, h=8, txt='Id Maestro', border=1, align='C', fill=True)
    pdf.cell(w=20, h=8, txt='Fecha', border=1, align='C', fill=True)
    pdf.cell(w=60, h=8, txt='Tipo de reporte', border=1, align='C', fill=True)
    pdf.multi_cell(w=0, h=8, txt='Nombre Archivo', border=1, align='C', fill=True)

    # ? Asignar el modelo
    reports = Reporte.objects.all()

    # ? Ciclar en el modelo
    for report in reports:
      pdf.set_font('Helvetica', '', 9)
      pdf.set_text_color(0)
      pdf.cell(w=10, h=7, txt=str(report.ciclo), border=1, align='C', fill=False)
      pdf.cell(w=40, h=7, txt=str(report.docentes), border=1, align='C', fill=False)
      pdf.cell(w=20, h=7, txt=str(report.fecha), border=1, align='C', fill=False)
      pdf.cell(w=60, h=7, txt=str(report.evidencia), border=1, align='C', fill=False)
      pdf.multi_cell(w=0, h=8, txt=str(report.titulo), border=1, align='C', fill=False)

  buffer = BytesIO()
  pdf.output(buffer)
  pdf_data = buffer.getvalue()
  
  return FileResponse(buffer, as_attachment=True, filename='Reporte.pdf')

  # Configurar el encabezado de la respuesta para descargar el archivo
  # response['Content-Disposition'] = 'attachment; filename="Reporte.pdf"'
  # return response

# ? Generar archivo de csv (excel)
def csv_report(request):
  response = HttpResponse(content_type='text/csv')
  response['Content-Disposition'] = 'attachment; filename="reporte.csv"'

  # ? Creae escritor csv
  writer = csv.writer(response)

  # ? Asignar el modelo
  reports = Reporte.objects.all()

  # ? Escribir texto de la primer casilla
  writer.writerow(['Titulo', 'Academia', 'Curso', 'Ciclo', 'Docente', 'Fecha'])

  # ? Ciclar en el modelo
  for report in reports:
    # docente_nombre = report.docentes.nombres if report.docentes else ''
    writer.writerow([report.titulo, report.academia, report.curso, report.ciclo, report.docentes, report.fecha])

  return response

# ? Generar archivo de texto
def text_report(request):
  response = HttpResponse(content_type='text/plain')
  response['Content-Disposition'] = 'attachment; filename="reporte.txt"'

  # ? Asignar el modelo
  reports = Reporte.objects.all()
  lines = []

  # ? Ciclar en el modelo
  for report in reports:
    lines.append(f'{report.titulo}\n{report.academia}\n{report.curso}\n{report.ciclo}\n{report.docentes}\n{report.fecha}\n\n\n')

  response.writelines(lines)
  return response

# ! Eliminar reporte
def delete_report(request, report_id):
  report = Reporte.objects.get(pk=report_id)
  report.delete()
  time.sleep(.5)
  return redirect('all_reports')

# ? Subir reportes
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

# ? Mostrar 1 solo reporte
def show_report(request, report_id):
  report = Reporte.objects.get(pk=report_id)
  form = ReportForm(request.POST or None, instance=report)
  if form.is_valid():
    form.save()
    time.sleep(1.5)
    return redirect('all_reports')

  return render(request, 'reports/show_report.html', {
    'report': report,
    'form': form,
  })

# ? Mostrar todos los reportes
def all_reports(request):
  report_list = Reporte.objects.all()

  return render(request, 'reports/report_list.html', {
    'report_list': report_list,
  })

# ? Mostrar página de inicio donde estan los menu
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