# Generated by Django 2.2 on 2019-05-27 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_project', models.IntegerField()),
                ('url', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('subtitle', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=60)),
                ('cover', models.CharField(max_length=60)),
            ],
        ),
    ]
