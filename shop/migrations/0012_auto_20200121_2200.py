# Generated by Django 2.2.5 on 2020-01-21 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_remove_product_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
