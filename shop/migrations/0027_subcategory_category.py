# Generated by Django 2.2.6 on 2020-03-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_remove_category_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='Category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='shop.Category'),
        ),
    ]
