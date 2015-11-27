# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('ts', models.DateTimeField(auto_now=True)),
                ('recepient', models.ForeignKey(related_name='recepient', to='app1.User')),
                ('sender', models.ForeignKey(related_name='sender', to='app1.User')),
            ],
        ),
    ]
