# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20150204_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reps',
            old_name='votes',
            new_name='reps',
        ),
    ]
