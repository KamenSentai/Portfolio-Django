from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'pages/index.html.jinja')

def about(request):
  return render(request, 'pages/about.html.jinja')

def contact(request):
  return render(request, 'pages/contact.html.jinja')

def error404(request, exception=None):
  return render(request, 'errors/404.html.jinja', {'error': exception}, status=404)
