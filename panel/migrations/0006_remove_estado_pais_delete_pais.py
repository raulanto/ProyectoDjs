# Generated by Django 4.2.6 on 2023-10-27 19:36

from django.db import migrations


class Migration(migrations.Migration):

    # dependencies = [
    #     ('panel', '0005_remove_estado_pais_alter_municipio_codigo_and_more'),
    # ]

    operations = [
        migrations.RemoveField(
            model_name='estado',
            name='pais',
        ),
        migrations.DeleteModel(
            name='Pais',
        ),
    ]