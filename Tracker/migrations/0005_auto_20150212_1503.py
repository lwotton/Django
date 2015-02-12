# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tastypie', '0001_initial'),
        ('admin', '0001_initial'),
        ('tracker', '0004_auto_20150211_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_ptr',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
