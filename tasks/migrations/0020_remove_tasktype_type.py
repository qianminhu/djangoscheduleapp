# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0019_tasktype_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktype',
            name='type',
        ),
    ]
