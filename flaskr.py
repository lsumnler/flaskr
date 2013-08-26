# all the imports
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
        render_template, flash

# configuration section
# A cleaner solution is to create a separate .py file and load that or
# or import values from there.
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application ;)
app = Flask(__name__)
app.config.from_object(__name__)

# database connection
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# this will initialize the sqlite3 database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# this will start the sever in standalone application
if __name__== '__main__':
    app.run()
