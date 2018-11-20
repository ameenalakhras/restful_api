from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT, jwt_required # to require a function for a key ### for authentication 

from securtiy import authenticate,identity # for JWT class


app = Flask(__name__)
app.secret_key="amin"
api = Api(app)

jwt = JWT(app,authenticate,identity)

items = []

class Item(Resource):


    # this code is like doing ### data = request.get_json() but better
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="this field can't be left blank")


    @jwt_required() # getting an item requires the authentication key
    def get(self,name):
        item = next(filter(lambda x : x['name']==name, items),None)
        return {'item':item}, 200 if item else 404


    def post(self,name):
        if  next(filter(lambda x : x['name']==name, items),None):
            return {"message":"an item with name {} already exists".format(name)},400 # bad request

        data = Item.parser.parse_args() # this is calling the RequestParser to get the json

        item = {'name':name,'price':data['price']}
        items.append(item)
        return item,201


    def delete(self,name):
        global items
        items = list(filter(lambda x : x['name'] != name, items))
        return {'message':'item deleted'}


    def put(self,name):
        item = next(filter(lambda x : x['name'] == name,items),None)

        data = Item.parser.parse_args()

        if item is None :
            item = {"name":name,"price":data["price"]}
            items.append(item)
        else :
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'all_items':items}

api.add_resource(Item,"/items/<string:name>")
api.add_resource(ItemList,"/items")



app.run(port=4000,debug=True)
