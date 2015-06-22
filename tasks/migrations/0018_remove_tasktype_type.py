# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_auto_20150619_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktype',
            name='type',
        ),
    ]
