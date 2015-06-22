# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_remove_tasktype_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currenttask',
            name='person_in_charge',
        ),
        migrations.AddField(
            model_name='tasktype',
            name='type',
            field=models.ForeignKey(to='tasks.CurrentTask'),
            preserve_default=False,
        ),
    ]
