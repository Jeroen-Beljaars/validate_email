from flask import Flask, render_template, request

from peewee import *

from functions import *
from sql import *


app = Flask(__name__, template_folder='.')


@app.route('/')
def no_mail():
    # If there is data in the database
    # Then create the table
    #  
    try:
        table = create_table(get_data())
    except:
        table = ""
    return render_template('index.html', table=table)


@app.route('/', methods=['POST'])
def check_input():
    # Get the data entered in the form
    email = request.form['text']

    # Check if the email syntax is valid or invalid
    outcome = check_email(email)

    # Add the data to the database
    set_data(email, outcome[0])

    # Update the table
    table = create_table(get_data())

    return render_template('index.html', result=outcome[1],
                           table=table)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

init_database()
