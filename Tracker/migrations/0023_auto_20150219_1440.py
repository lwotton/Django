# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0022_activity_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='reps',
        ),
        migrations.AddField(
            model_name='activity',
            name='reps',
            field=models.IntegerField(default=0, max_length=3),
            preserve_default=True,
        ),
    ]
