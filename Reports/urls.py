from django.urls import path
from . import views

urlpatterns = [
  path('inicio/', views.inicio, name='inicio'),
  path('about', views.about, name='about'),
  path('<int:year>/<str:month>/', views.inicio, name='inicio'),
  path('reports/', views.all_reports, name='all_reports'),
  path('show_report/<report_id>', views.show_report, name='show-report'),
  path('upload/', views.upload_docs, name='upload_docs'),
]
