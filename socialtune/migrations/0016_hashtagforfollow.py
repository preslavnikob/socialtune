# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialtune', '0015_auto_20170322_0546'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashtagForFollow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialtune.Users')),
            ],
        ),
    ]
