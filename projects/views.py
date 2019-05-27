from django.http import HttpResponse
from django.shortcuts import render

from .models import ProjectModel

def index(request):
    projects = ProjectModel.objects.all()
    return render(request, 'projects/index.html.jinja', {
        'h1': 'All my projects',
        'h2': 'Discover everything I have done so far',
        'projects': projects
    })

def project(request, slug):
    project = ProjectModel.objects.get(slug=slug)
    return render(request, 'projects/project.html.jinja', {
        'h1': project.title,
        'h2': project.subtitle,
        'project': project
    })
