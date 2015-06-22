# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20150617_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenttask',
            name='person_in_charge',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
