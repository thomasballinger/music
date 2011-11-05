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


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'development key'

@app.route('/')
def frontpage():
    return render_template('frontpage.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run('0.0.0.0', port=port)
