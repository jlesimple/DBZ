# Generated by Django 4.1.1 on 2022-09-19 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_place_place_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='activity',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='birth',
            field=models.IntegerField(default=0),
        ),
    ]
