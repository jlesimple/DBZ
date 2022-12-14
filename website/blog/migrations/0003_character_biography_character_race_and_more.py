# Generated by Django 4.1.1 on 2022-09-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_saga'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='character',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='characters'),
        ),
    ]
