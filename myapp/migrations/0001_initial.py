# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateTimeField()),
                ('ggirlnum', models.IntegerField()),
                ('gboynum', models.IntegerField()),
                ('isDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Studengts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('sgender', models.BooleanField()),
                ('sage', models.IntegerField()),
                ('sxontend', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField()),
                ('sgrade', models.ForeignKey(to='myapp.Grades')),
            ],
        ),
    ]
