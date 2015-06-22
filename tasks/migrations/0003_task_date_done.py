# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150615_2335'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date_done',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 15, 23, 43, 41, 937247, tzinfo=utc), verbose_name=b'date due'),
            preserve_default=False,
        ),
    ]
