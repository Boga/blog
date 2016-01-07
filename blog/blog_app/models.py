from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from markdown import markdown
from slugify import slugify
from taggit.managers import TaggableManager


class Note(models.Model):
    """
    Attributes:
        title The maximum speed that such a bird can attain.
        body  The locale where these birds congregate to reproduce.
    """
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(max_length=4000, blank=True, db_index=True)
    body_html = models.TextField(max_length=4000, blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    tags = TaggableManager(blank=True)
    url = models.CharField(max_length=2000, default=None, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url = slugify(self.title)
        # self.body_html = markdown(self.body)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return '%r %s' % (self.id, self.title)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        ordering = ('-pub_date',)


class AttachedFile(models.Model):
    file = models.FileField(upload_to='%Y/%m/%d/')
    note = models.ForeignKey(Note, on_delete=models.CASCADE,
                             related_name='attaches')
