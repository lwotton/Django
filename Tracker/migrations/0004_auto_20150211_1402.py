# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('tracker', '0003_auto_20150204_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('timezone', models.CharField(default=b'Europe/London', max_length=50)),
                ('exercise', models.ForeignKey(to='tracker.Exercise')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.RemoveField(
            model_name='reps',
            name='exercise',
        ),
        migrations.DeleteModel(
            name='Reps',
        ),
        migrations.AddField(
            model_name='exercise',
            name='reps',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='weight',
            field=models.CharField(default=0, max_length=100),
            preserve_default=True,
        ),
    ]
