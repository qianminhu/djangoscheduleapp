# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20150615_1735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Detail',
            new_name='TaskRenameTest',
        ),
        migrations.RenameModel(
            old_name='Task',
            new_name='Template',
        ),
    ]
