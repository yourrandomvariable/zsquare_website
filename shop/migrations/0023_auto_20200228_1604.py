# Generated by Django 2.2.6 on 2020-02-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20200228_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]