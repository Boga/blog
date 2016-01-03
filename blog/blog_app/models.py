from __future__ import unicode_literals

from markdown import markdown
from taggit.managers import TaggableManager
from django.db import models
from django.utils import timezone
from slugify import slugify


class Note(models.Model):
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(max_length=4000, blank=True)
    body_html = models.TextField(max_length=4000, blank=True, editable = False)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    tags = TaggableManager(blank=True)
    url = models.CharField(max_length=2000, default=None, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url = slugify(self.title)
        self.body_html = markdown(self.body)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return '%r %s' % (self.id, self.title)

    def __unicode__(self):
        return '%r %s' % (self.id, self.title)

    class Meta:
        ordering = ('-pub_date',)
