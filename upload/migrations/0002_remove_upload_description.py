# Generated by Django 2.2.6 on 2020-02-28 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upload',
            name='description',
        ),
    ]
