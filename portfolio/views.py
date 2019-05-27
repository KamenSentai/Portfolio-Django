from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')

def contact(request):
  return render(request, 'pages/contact.html')

def error404(request, exception=None):
  return render(request, 'errors/404.html', {'error': exception}, status=404)
