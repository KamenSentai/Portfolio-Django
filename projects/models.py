from django.db import models

class ProjectModel(models.Model):
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='static/images')
    date = models.DateField()
    role = models.CharField(max_length=60)
    description = models.TextField()
    link = models.URLField(max_length=60)
