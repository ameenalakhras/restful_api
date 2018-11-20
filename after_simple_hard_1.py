from flask import Flask,request
from flask_restful import Resource,Api,reqparse
# to require a function for a key ### for authentication
from flask_jwt import JWT, jwt_required
# for JWT class
from security import authenticate,identity

from resources.item import Item,ItemList
from resources.user import UserRegister
from models.user import UserModel

app = Flask(__name__)
# locating the databse for SQLAlchemy (doesn't have to be sqlite3 it can be any databse)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# turning off flask-SQLAlchemy modifications since it's in SQLAlchemy origionally existing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="amin"
api = Api(app)

# create all tables(and db) before first request if they don't exist
@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app,authenticate,identity)


api.add_resource(Item,"/items/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister,'/register')


if __name__ == "__main__":
    from db import db # import the database
    db.init_app(app)

    app.run(port=4000,debug=True)
