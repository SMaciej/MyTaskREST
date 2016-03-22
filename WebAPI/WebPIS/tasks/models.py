# -*- coding: utf-8 -*-
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
#from django.contrib.auth.models import User

class Task(models.Model):
    PRIORITIES = ((1, 'Niski'),(2, 'Normalny'),(3, 'Wysoki'),)

    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=2, choices=PRIORITIES)
    owner = models.ForeignKey('auth.User', related_name='tasks')

