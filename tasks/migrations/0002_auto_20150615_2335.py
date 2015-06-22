# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='person_name',
            new_name='person_in_charge',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='task',
        ),
    ]
