# Generated by Django 4.1.2 on 2022-11-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellidoP', models.CharField(max_length=50, verbose_name='Apellido paterno')),
                ('apellidoM', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('FecNac', models.DateField()),
                ('dir_id', models.IntegerField()),
                ('Usuario_activo', models.BooleanField(default=True)),
                ('Usuario_administrador', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo electronico')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]