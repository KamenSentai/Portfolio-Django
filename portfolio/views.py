from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return render(request, 'pages/index.html.jinja', {
    'h1': 'Alain Cao Van Truong',
    'h2': 'Full-stack developer & web student',
  })

def about(request):
  return render(request, 'pages/about.html.jinja', {
    'h1': 'About myself',
    'h2': 'Learn about what I like doing',
  })

def contact(request):
  return render(request, 'pages/contact.html.jinja', {
    'h1': 'Contact me',
    'h2': 'See how to find me',
  })

def error404(request, exception=None):
  return render(request, 'errors/404.html.jinja', {'error': exception}, status=404)
