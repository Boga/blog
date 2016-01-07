#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
from oauth2client import client
from googleapiclient import sample_tools


def main(argv):
    # Authenticate and construct service.
    scope = 'https://www.googleapis.com/auth/blogger'
    service, flags = sample_tools.init(argv, 'blogger', 'v3', __doc__, __file__,
                                       scope=scope)

    try:

        users = service.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()
        print('This user\'s display name is: %s' % thisuser['displayName'])

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()
        blog = thisusersblogs['items'][0]
        print('The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))
        posts = service.posts()
        request = posts.list(blogId=blog['id'])
        while request != None:
            posts_doc = request.execute()
            if 'items' in posts_doc and not (posts_doc['items'] is None):
                for post in posts_doc['items']:
                    note = {
                        'pub_date': post['published'],
                        'title': post['title'],
                        'body_html': post['content'],
                    }

                    for tag in post['labels']:

                    print(note)
                request = posts.list_next(request, posts_doc)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run'
              'the application to re-authorize')


if __name__ == '__main__':
    main(sys.argv)
