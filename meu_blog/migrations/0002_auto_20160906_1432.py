# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-06 17:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artigo',
            options={'ordering': ('-publicacao',)},
        ),
        migrations.AlterField(
            model_name='artigo',
            name='publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 9, 6, 14, 32, 27, 167775)),
        ),
    ]
