# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20150616_1020'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaskRenameTest',
            new_name='CurrentTask',
        ),
    ]
