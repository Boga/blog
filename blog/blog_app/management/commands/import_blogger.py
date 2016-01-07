#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from blog_app.models import Note
from django.core.management.base import BaseCommand
from googleapiclient import sample_tools
from oauth2client import client


class Command(BaseCommand):
    '''
    Imports data from Blogger into this app. Retrievs users first blog only.
    Necessary credentials you can get from https://console.developers.google.com/apis/credentials
    '''

    def handle(self, *args, **options):
        # Authenticate and construct service.
        scope = 'https://www.googleapis.com/auth/blogger'
        service, flags = sample_tools.init([], 'blogger', 'v3', __doc__,
                                           __file__, scope=scope)

        try:
            users = service.users()
            thisuser = users.get(userId='self').execute()
            print('This user\'s display name is: %s' % thisuser['displayName'])
            blogs = service.blogs()
            thisusersblogs = blogs.listByUser(userId='self').execute()
            blog = thisusersblogs['items'][0]
            print(
                'The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))
            Note.objects.all().delete()
            posts = service.posts()
            request = posts.list(blogId=blog['id'])
            while request != None:
                posts_doc = request.execute()
                if 'items' in posts_doc and not (posts_doc['items'] is None):
                    for post in posts_doc['items']:
                        note = Note(title=post['title'], pub_date=post[
                            'published'], body_html=post['content'])
                        note.save()
                        for tag in post['labels']:
                            note.tags.add(tag)
                        print(note.title)
                    request = posts.list_next(request, posts_doc)

        except client.AccessTokenRefreshError:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize')
