# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

from services.pbiembedservice import PbiEmbedService
from utils import Utils
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session
import json
import os

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'PBISample' #secret for session 
# Load configuration
app.config.from_object('config.BaseConfig')

@app.route('/')
def index():
    #adding to redirect default to login instead of index
    return redirect(url_for('login'))
    '''Returns a static HTML page'''
    #return render_template('index.html')
# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == '':            
            error = 'Invalid Credentials. Please try again.'
        else:
            user_name = request.form['username']
            session['username'] = request.form['username']
            return redirect(url_for('home', username=user_name))
    return render_template('login.html', error=error)
# def login_form():
#     '''Returns a static HTML page'''
#     return render_template('login.html')
# @app.route('/login', methods=['POST'])
# def login_form_post():
#     '''Returns a static HTML page'''
#     customer_name = request.form("customerName")
#     cust = customer()
#     return customer_name
@app.route('/home')
def home():
    username = None
    if 'username' in session:
        username = session['username'] #session.pop('username', None) #example users: Kevin Liu Cory Booth Guy Gilbert Anthony Chor
    '''Returns a static HTML page'''
    return render_template('home.html', username=username)

@app.route('/getembedinfo', methods=['GET'])
def get_embed_info():
    '''Returns report embed configuration'''
    username = None
    if 'username' in session:
        username = session['username']
    config_result = Utils.check_config(app)
    if config_result is not None:
        return json.dumps({'errorMsg': config_result}), 500

    try:
        embed_info = PbiEmbedService().get_RLSembed_params_for_single_report(app.config['WORKSPACE_ID'], app.config['REPORT_ID'], loggedin_user = username)
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500

@app.route('/favicon.ico', methods=['GET'])
def getfavicon():
    '''Returns path of the favicon to be rendered'''

    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run()