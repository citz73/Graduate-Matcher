# Generated by Django 2.2.7 on 2019-12-02 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradmatchapp', '0003_auto_20191202_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]
