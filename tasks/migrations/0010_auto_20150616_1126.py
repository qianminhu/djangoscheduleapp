# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_auto_20150616_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currenttask',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='currenttask',
            name='type',
        ),
        migrations.AddField(
            model_name='currenttask',
            name='date_done',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 18, 25, 48, 213682, tzinfo=utc), verbose_name=b'date due'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currenttask',
            name='email',
            field=models.EmailField(default=b'ENTER EMAIL', max_length=254),
        ),
        migrations.AddField(
            model_name='currenttask',
            name='frequency',
            field=models.CharField(choices=[(b'One Time', b'One Time'), (b'Weekly', b'Weekly'), (b'Monthly', b'Monthly')], default=b'One Time', max_length=10),
        ),
        migrations.AddField(
            model_name='currenttask',
            name='person_in_charge',
            field=models.CharField(default='Enter Person in Charge', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currenttask',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2015, 6, 16, 18, 26, 10, 206584, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currenttask',
            name='task',
            field=models.CharField(default='Enter type of task', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='currenttask',
            name='description',
            field=models.CharField(max_length=254),
        ),
        migrations.DeleteModel(
            name='Template',
        ),
    ]
