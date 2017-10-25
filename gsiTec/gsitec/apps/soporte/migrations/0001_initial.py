# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('prioridad', models.IntegerField()),
                ('asunto', models.CharField(max_length=100)),
                ('mensage', models.TextField(max_length=1000)),
                ('archivo', models.FileField(null=True, upload_to=b'', blank=True)),
                ('servicio', models.CharField(max_length=100)),
            ],
        ),
    ]
