from django.http import HttpResponse
from django.shortcuts import render

from .mocks import Projects

def index(request):
  projects = Projects.all()
  return render(request, 'projects/index.html.jinja', {'projects': projects})

def project(request, slug):
  project = Projects.find(slug)
  return render(request, 'projects/project.html.jinja', {'project': project})
