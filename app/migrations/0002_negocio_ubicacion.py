# Generated by Django 4.0.6 on 2022-09-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='ubicacion',
            field=models.TextField(null=True),
        ),
    ]