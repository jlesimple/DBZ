# Generated by Django 4.1.1 on 2022-09-17 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_character_biography_character_race_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='saga',
            name='biography',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='saga',
            name='chap_start',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='saga',
            name='chap_stop',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='saga',
            name='resume',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='saga',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='characters'),
        ),
    ]