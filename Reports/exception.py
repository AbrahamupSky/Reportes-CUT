from django.http import HttpResponseNotFound
from django.template.loader import get_template

def handle404(request, exception):
  template = get_template('404.html')
  return HttpResponseNotFound(template.render(request))