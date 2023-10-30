from django.contrib import admin
from django.urls import path, include

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('Reports.urls')),
  path('docentes/', include('django.contrib.auth.urls')),
  path('docentes/', include('Docentes.urls')),
]