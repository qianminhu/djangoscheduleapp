# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_auto_20150616_1015'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskrenametest',
            old_name='email',
            new_name='owner',
        ),
        migrations.RemoveField(
            model_name='taskrenametest',
            name='person_in_charge',
        ),
        migrations.AddField(
            model_name='template',
            name='email',
            field=models.EmailField(default=b'ENTER EMAIL', max_length=254),
        ),
        migrations.AddField(
            model_name='template',
            name='person_in_charge',
            field=models.CharField(default=b'ENTER PERSON IN CHARGE', max_length=255),
        ),
    ]
