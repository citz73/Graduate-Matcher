# Generated by Django 3.0 on 2019-12-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradmatchapp', '0010_auto_20191208_1608'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='deadline',
            field=models.ManyToManyField(to='gradmatchapp.Deadline'),
        ),
    ]
