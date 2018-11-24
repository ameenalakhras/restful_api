# this file is made because the server runs uwsgi.ini and not app.py so it can't import db, therefor now it can.

from db import db # import the database
from app import app


db.init_app(app)

# create all tables(and db) before first request if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()
