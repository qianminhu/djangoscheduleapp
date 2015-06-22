# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_date_done'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Frequency',
        ),
        migrations.AddField(
            model_name='task',
            name='frequency',
            field=models.CharField(choices=[(b'One Time', b'One Time'), (b'Weekly', b'Weekly'), (b'Monthly', b'Monthly')], default=b'One Time', max_length=10),
        ),
    ]
