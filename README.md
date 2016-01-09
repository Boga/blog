System-wide requirements:

+   python-dev 
+   python-virtualenv
+   libjpeg-dev

You might also be interested in installation of some database-specific 
packages (i.e. `python2.7-psycopg2 postgresql-server-dev-9.3` for PostgreSQL). 

Python requirements are listed in requirements.txt

You have to create blog/blog/settings/__init__.py and point there  
configuration file you want to use. Also, you can override some settings 
(i.e. SECRET_KEY):

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from __future__ import absolute_import
    from .dev import *
    
    SECRET_KEY = '0fly3^1*cf(25(vg_@d=e$e*#d77#1=n)d60-f9_2!98p$phz('
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db', 'db.sqlite3'),
        }
    }
