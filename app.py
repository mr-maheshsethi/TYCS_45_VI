from flask import Flask, redirect, url_for, request
import flask
import functools
import json
import os

from authlib.client import OAuth2Session
import google.oauth2.credentials
import googleapiclient.discovery

import google_auth

app = flask.Flask(__name__)
app.secret_key = os.environ.get("FN_FLASK_SECRET_KEY", default=False)

app.register_blueprint(google_auth.app)

@app.route('/')
def index():
    if google_auth.is_logged_in():
        user_info = google_auth.get_user_info()
        return '<div>You are currently logged in as ' + user_info['given_name'] + '<div><pre>' + json.dumps(user_info, indent=4) + "</pre>"

    return 'You are not currently logged in.'


@app.route('/output/<name>')
def output(name):
    return 'Welcome %s' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('output', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('output', name= user))


@app.route('/terminal')
def terminal():
    return 'terminal'

@app.route('/devices_connected')
def device_manager():
    return 'Thisi is my device manager'

if __name__ == '__main__':
    app.run(debug = True)
    
