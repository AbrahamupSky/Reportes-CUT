from django.urls import path
from . import views

urlpatterns = [
  path('inicio/', views.inicio, name='inicio'),
  path('<int:year>/<str:month>/', views.inicio, name='inicio'),
  path('reports/', views.all_reports, name='all_reports'),
  path('upload/', views.upload_docs, name='upload_docs'),
]
