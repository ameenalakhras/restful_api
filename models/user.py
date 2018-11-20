import sqlite3
from db import db


class UserModel(db.Model): # importing SQLAlchemy database to be used
    __tablename__ = 'users' #SQLAlchemy tablename
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,username,password):

        self.username = username
        self.password = password


    @classmethod
    def find_by_id(cls,_id):
        cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls,username):
        ### cls hers is like writing ItemModel
        return cls.query.filter_by(username=username).first() ## it's like : SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
