# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal_name', models.CharField(max_length=200)),
                ('animal_birth', models.DateTimeField(verbose_name=b'date birth')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_name', models.CharField(max_length=200)),
                ('person_email', models.EmailField(max_length=30)),
                ('person_details', models.CharField(max_length=3000)),
                ('person_views', models.IntegerField(default=0)),
                ('person_pet', models.ForeignKey(to='animals.Animal')),
            ],
        ),
    ]
