from __future__ import unicode_literals
from taggit.managers import TaggableManager
from django.db import models
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(max_length=4000, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return '%r %s' % (self.id, self.title)

    class Meta:
        ordering = ('pub_date',)
