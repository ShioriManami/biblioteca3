# Generated by Django 4.1.2 on 2022-11-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='Numero',
            field=models.IntegerField(verbose_name='Numero'),
        ),
    ]