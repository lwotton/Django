# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_remove_userprofile_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
