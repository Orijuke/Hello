import os
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for
from hello.data import db_session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


@app.route('/')
def index():
	db = db_session.create_session()
	return render_template("public.html")


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)