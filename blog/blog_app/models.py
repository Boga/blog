from __future__ import unicode_literals

from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=4000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '%r %s' % (self.id, self.title)