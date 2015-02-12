# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20150212_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='exercise_name',
            new_name='exercise',
        ),
        migrations.RenameField(
            model_name='exercise',
            old_name='userID',
            new_name='person',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='timezone',
        ),
        migrations.AddField(
            model_name='exercise',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 15, 53, 0, 957920, tzinfo=utc), verbose_name=b'date done'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 15, 53, 16, 177157, tzinfo=utc), verbose_name=b'date created'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
