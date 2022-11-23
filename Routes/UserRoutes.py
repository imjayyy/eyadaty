from flask import Blueprint, Flask, render_template, url_for, request, session, redirect, flash, Markup

import os
import pathlib
import requests
import pymongo
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from oauthlib.oauth2 import WebApplicationClient
from Models.users import User
from classes.connection import send_email

from werkzeug.utils import secure_filename
from flask_mail import Mail, Message




home_routes = Blueprint('home_routes', __name__)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "451555908886-stms5lvelo7jbdds3ihdau8iaq323p79.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
    # "http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return redirect('/')  # Authorization required
        else:
            return function()
    wrapper.__name__ = function.__name__
    return wrapper


@home_routes.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!
    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)
    id_info = id_token.verify_oauth2_token(
              id_token=credentials._id_token,
              request=token_request,
              audience=GOOGLE_CLIENT_ID)
    User.signUpAndLoginUser(id_info.get("name"), id_info.get('email'), id_info.get("sub") )

    return id_info


@home_routes.route("/GoogleSignIn")
def goooglesignin():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)

@home_routes.route("/updateInfo", methods = ['GET', 'POST'])
@login_is_required
def updateInfo():
    if request.method == 'POST':
        User.updateInfo(session['Email'], session["google_id"], request.form['Phone'])
        if request.files['file']:
            if request.files['file'].filename!='':
                file = request.files['file']
                newname = file.filename.split('.')
                newname = session['Email'] + '.' + newname[1]
                file.filename = newname
                filename = secure_filename(file.filename)
                file.save(os.path.join('static/uploads/' , filename))
        session['Phone'] = request.form['Phone']   
        return redirect("/dashboard")
    return render_template('user_updateinfo.html')

@home_routes.route("/dashboard")
@login_is_required
def dashboard():
    return session

@home_routes.route("/analytics")
@login_is_required
def analytics():
    return 'Page 2'

