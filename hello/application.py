import os
from datetime import timedelta
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


@app.route('/')
def index():
    return render_template("public.html", news=news)


def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)