#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import sys

from googleapiclient.discovery import build
from oauth2client import client
from googleapiclient import sample_tools
from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials

client_id='blogger2egea'
secret_key='AIzaSyDwCNOwZ6Tq6pNjVq_UZMWpn_kh--UXYLI'

f = open('client_secrets.json')
data = json.load(f)
credentials = SignedJwtAssertionCredentials(data["client_email"],
                                            data["private_key"],
                                            'https://www.googleapis.com/auth/blogger')
http = Http()
credentials.authorize(http)

blogger = build(serviceName='blogger', version='v3', http=http)
users = blogger.users()
thisuser = users.get(userId='self').execute()

blogs = blogger.blogs()
thisusersblogs = blogs.listByUser(userId='self').execute()
for blog in thisusersblogs['items']:
    print('The blog named \'%s\' is at: %s' % (blog['name'], blog['url']))

posts = blogger.posts()

