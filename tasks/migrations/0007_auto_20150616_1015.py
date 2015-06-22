# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20150615_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskrenametest',
            old_name='owner',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='template',
            name='email',
        ),
        migrations.RemoveField(
            model_name='template',
            name='person_in_charge',
        ),
        migrations.AddField(
            model_name='taskrenametest',
            name='person_in_charge',
            field=models.CharField(default=b'DEFAULT VALUE', max_length=255),
        ),
    ]
