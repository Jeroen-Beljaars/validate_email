from flask import Flask, render_template, request
from functions import *

app = Flask(__name__, template_folder='.')

@app.route('/')
def no_mail():
    return render_template('index.html', email = "Enter email here")

@app.route('/', methods=['POST'])
def check_input():
    print("workings")
    email = request.form['text']
    return render_template('index.html', result = check_email(email))

@app.route('/<email>')
def send_check_mail(email):
    return render_template('index.html', result = check_email(email))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8000")