"""
Create the database
Add data to database
Get data from database
"""

from peewee import *
from functions import *


# Create the database
db = SqliteDatabase('check_history.db')


class Check_history(Model):
    """Create the columns"""
    email = CharField()
    valid_or_invalid = CharField(max_length=10)

    class Meta:
        """
        Tell the class Check_history that
        The data belongs to the database check_history
        """
        database = db


def set_data(email, valid_invalid):
    """Add the given data to database"""
    data = Check_history.create(email=email,
                                valid_or_invalid=valid_invalid)
    data.save()


def get_data():
    """Get all the data from the database"""
    data_list = []
    for email in Check_history.select():
        data_list.append([email.email, email.valid_or_invalid])
    return data_list


def init_database():
    """initialize the database"""
    db.connect()
    db.create_tables([Check_history], safe=True)
