# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20150212_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 12, 16, 56, 11, 12362, tzinfo=utc), verbose_name=b'date done'),
            preserve_default=True,
        ),
    ]
