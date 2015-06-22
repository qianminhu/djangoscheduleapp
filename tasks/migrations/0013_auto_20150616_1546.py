# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20150616_1147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currenttask',
            old_name='date_done',
            new_name='date_due',
        ),
    ]
