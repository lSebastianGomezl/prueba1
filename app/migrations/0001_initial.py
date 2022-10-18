# Generated by Django 4.0.6 on 2022-09-22 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Negocio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='negocios')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='negocios', to=settings.AUTH_USER_MODEL)),
                ('tipo_Negocio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_negocio')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('nuevo', models.BooleanField()),
                ('imagen', models.ImageField(null=True, upload_to='negocios/items')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('negocio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_negocio')),
            ],
        ),
    ]
