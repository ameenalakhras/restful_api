import os

from flask import Flask,request
from flask_restful import Resource,Api,reqparse
# to require a function for a key ### for authentication
from flask_jwt import JWT, jwt_required
# for JWT class
from security import authenticate,identity

from resources.item import Item,ItemList
from resources.user import UserRegister,UserList
from resources.store import Store,StoreList
# from models.user import UserModel


app = Flask(__name__)
# locating the databse for SQLAlchemy (doesn't have to be sqlite3 it can be any databse)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
# turning off flask-SQLAlchemy modifications since it's in SQLAlchemy origionally existing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="amin"
api = Api(app)



jwt = JWT(app,authenticate,identity)


api.add_resource(Item,"/items/<string:name>")
api.add_resource(ItemList,"/items")
api.add_resource(UserRegister,'/register')
api.add_resource(UserList,'/users')
api.add_resource(Store,"/store/<string:name>")
api.add_resource(StoreList,'/stores')


if __name__ == "__main__":
    from db import db # import the database
    db.init_app(app)

    app.run(port=4000,debug=True)
