# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20150615_1734'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Detail',
        ),
    ]
