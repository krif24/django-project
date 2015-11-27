# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=200)),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'f', b'Female'), (b'm', b'Male'), (b'n', b'N/A')])),
                ('age', models.DecimalField(max_digits=2, decimal_places=0)),
                ('photo', models.FileField(upload_to=b'photos')),
                ('active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(to='app1.Group')),
            ],
        ),
    ]
