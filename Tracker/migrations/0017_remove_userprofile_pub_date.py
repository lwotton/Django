# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_auto_20150212_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='pub_date',
        ),
    ]
