# Generated by Django 4.1.1 on 2022-09-22 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_race_character_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saga',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
