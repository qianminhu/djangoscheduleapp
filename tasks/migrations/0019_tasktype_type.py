# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0018_remove_tasktype_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktype',
            name='type',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 19, 20, 24, 30, 502450, tzinfo=utc), to='tasks.CurrentTask'),
            preserve_default=False,
        ),
    ]
