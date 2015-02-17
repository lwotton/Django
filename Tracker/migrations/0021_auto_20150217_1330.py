# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0020_auto_20150216_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='exercise',
            field=models.ForeignKey(to='tracker.Exercise'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
