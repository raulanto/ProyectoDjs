# Generated by Django 4.2.6 on 2023-10-25 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0002_remove_estado_pais_delete_pais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='nombre',
            field=models.CharField(max_length=250),
        ),
    ]