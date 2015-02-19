# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0021_auto_20150217_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='weight',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
