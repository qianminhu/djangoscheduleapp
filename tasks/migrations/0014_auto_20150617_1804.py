# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_auto_20150616_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=600)),
            ],
        ),
        migrations.RemoveField(
            model_name='currenttask',
            name='description',
        ),
        migrations.AddField(
            model_name='tasktype',
            name='type',
            field=models.ForeignKey(to='tasks.CurrentTask'),
        ),
    ]
