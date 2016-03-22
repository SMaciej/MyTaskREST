# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=2, choices=[(1, b'Niski'), (2, b'Normalny'), (3, b'Wysoki')])),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(related_name=b'snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
