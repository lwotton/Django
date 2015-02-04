# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('exercise', models.ForeignKey(to='tracker.Exercise')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exercise',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 2, 4, 15, 30, 27, 960171, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
