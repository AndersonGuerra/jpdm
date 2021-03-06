# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaur_management', '0002_dinossauro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimentacao',
            name='tipo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dinossauro',
            name='nome_br',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='especie',
            name='nome',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='genero',
            name='nome',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='ordem',
            name='nome',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='subordem',
            name='nome',
            field=models.CharField(max_length=250),
        ),
    ]
