#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.views import View
from flask import render_template
from datetime import datetime


class Note(View):
    def dispatch_request(self):
        data = {
            'date': datetime.now()
        }
        return render_template('about.jinja2', data=data)