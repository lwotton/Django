# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_exercise_reps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='exercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='userID',
            field=models.ForeignKey(default=1, to='tracker.UserProfile'),
            preserve_default=False,
        ),
    ]
