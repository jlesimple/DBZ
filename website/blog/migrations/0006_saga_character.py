# Generated by Django 4.1.1 on 2022-09-17 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_character_race'),
    ]

    operations = [
        migrations.AddField(
            model_name='saga',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.character'),
        ),
    ]
