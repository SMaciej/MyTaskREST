# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160101_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(default=b'not', max_length=4, choices=[(b'done', b'Wykonane'), (b'not', b'Niewykonane')]),
        ),
    ]
