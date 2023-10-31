from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('Reports.urls')),
  path('', RedirectView.as_view(url='docentes/login_user/'), name='redirect_to_login'),
  path('docentes/', include('django.contrib.auth.urls')),
  path('docentes/', include('Docentes.urls')),
]