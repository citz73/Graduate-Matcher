# Generated by Django 3.0 on 2019-12-08 07:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gradmatchapp', '0006_auto_20191207_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='user',
        ),
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]