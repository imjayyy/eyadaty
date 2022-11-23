from flask import Flask, render_template, session, redirect, url_for
from Routes.UserRoutes import home_routes
from classes.connection import mail

app = Flask(__name__)

# app.secret_key = '1lswqa'

app.config.from_object("config.Config") 

app.register_blueprint(home_routes)

mail.init_app(app)


@app.route('/')
def home():
    return "Welcome to Eyadaty APIs"



if __name__ == '__main__':
    app.run(debug=True)