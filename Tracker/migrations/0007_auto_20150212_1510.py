# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='reps',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='exercise',
            field=models.ForeignKey(default=1, to='tracker.Exercise'),
            preserve_default=False,
        ),
    ]
