# Generated by Django 2.2 on 2019-05-27 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_projectmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='link',
            field=models.URLField(max_length=60),
        ),
    ]
