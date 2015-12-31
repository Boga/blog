#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from views import about, note

app = Flask(__name__)
app.debug = True

notes = [
    {
        'id': 1,
        'title': 'First note title',
        'body': 'First note large body',
    },
    {
        'id': 2,
        'title': 'Second note title',
        'body': 'Second note large body',
    },
    {
        'id': 3,
        'title': 'Third note title',
        'body': 'Third note large body',
    },
    {
        'id': 4,
        'title': 'Fourth note title',
        'body': 'Fourth note large body',
    },
]


@app.route('/')
def list_notes():
    return render_template('notes.jinja2', notes=notes)


@app.route('/note/<note_id>')
def show_note(note_id):
    note_id = int(note_id)
    note = None
    for cur_note in notes:
        if cur_note['id'] == note_id:
            note = cur_note
    print(note_id)
    return render_template('note.jinja2', note=note)

app.add_url_rule('/', view_func=note.Note.as_view('notes'))
app.add_url_rule('/about', view_func=about.About.as_view('about'))

if __name__ == '__main__':
    app.run()
