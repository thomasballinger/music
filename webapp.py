#!/usr/bin/env python

import pprint
import os
import cPickle as pickle
from flask import Flask
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash
from flask import make_response

from pyechonest.util import EchoNestAPIError

import caption
import lolspeak
import nest

MAX_RETRIES = 2

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']

@app.route('/lolartist/about')
def aboutpage():
    return render_template('frontpage.html')

@app.route('/lolartist/<artist_name>')
def lolartist(artist_name, attempt_number=1):
    if attempt_number > MAX_RETRIES + 1:
        return render_template('try_another.html')
    try:
        song_titles = nest.get_songs(artist_name)
        fname = nest.get_pic(artist_name)
        fobj = caption.pasteTextOntoImage(fname, song_titles)
        response = make_response(fobj.read())
        response.headers['Content-Type'] = 'image/jpeg'
        #response.headers['Content-Disposition'] = 'attachment; filename=kitteh.jpg'
        return response
    except EchoNestAPIError:
        return render_template('try_another.html')
    except IOError:
        return lolartist(artist_name, attempt_number = attempt_number + 1)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
