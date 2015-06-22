# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_auto_20150616_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttask',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
