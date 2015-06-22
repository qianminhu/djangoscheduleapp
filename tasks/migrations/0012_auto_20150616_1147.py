# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20150616_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttask',
            name='date_done',
            field=models.DateTimeField(verbose_name=b'date due'),
        ),
        migrations.AlterField(
            model_name='currenttask',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'date published'),
        ),
    ]
