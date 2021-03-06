# Generated by Django 2.2 on 2019-05-27 19:59

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20190527_1954'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/static/images'), upload_to='')),
                ('description', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('subtitle', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
