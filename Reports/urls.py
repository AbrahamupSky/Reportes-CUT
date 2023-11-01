from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('inicio/', views.inicio, name='inicio'),
  path('about', views.about, name='about'),
  path('<int:year>/<str:month>/', views.inicio, name='inicio'),
  path('reports/', views.all_reports, name='all_reports'),
  path('reports/teachers/', views.specific_reports, name='specific_reports'),
  path('show_report/<report_id>', views.show_report, name='show-report'),
  path('upload/', views.upload_docs, name='upload_docs'),
  path('delete_report/<report_id>', views.delete_report, name='delete-report'),
  path('general_report', views.general_report, name='general_report'),
  path('text_report', views.text_report, name='text_report'),
  path('csv_report', views.csv_report, name='csv_report'),
  path('pdf_report', views.pdf_report, name='pdf_report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)