# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20160101_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=2, choices=[(1, b'Wykonane'), (2, b'Niewykonane')]),
        ),
    ]
