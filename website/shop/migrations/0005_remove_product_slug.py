# Generated by Django 4.1.1 on 2022-09-22 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]