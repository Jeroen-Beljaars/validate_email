from flask import Flask, render_template, request
import sqlite3

from peewee import *

from functions import *
from sql import *

app = Flask(__name__, template_folder='.')

@app.route('/')
def no_mail():
    return render_template('index.html', email = "Enter email here")

@app.route('/', methods=['POST'])
def check_input():
    email = request.form['text']
    outcome = check_email(email)
    set_data(email, outcome)
    result_set = get_data()
    print(result_set + "------------")
    return render_template('index.html', result = outcome)

@app.route('/<email>')
def send_check_mail(email):
    outcome = check_email(email)
    set_data(email, outcome)
    result_set = get_data()
    return render_template('index.html', result = outcome)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    init_database()    