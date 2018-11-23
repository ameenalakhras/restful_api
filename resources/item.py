from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.item import ItemModel



class Item(Resource):

    # this code is like doing ### data = request.get_json() but better
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type=float,
    required=True,
    help="this field can't be left blank")
    parser.add_argument('store_id',
    type=int,
    required=True,
    help="an item without a store can't be made!")


    @jwt_required() # getting an item requires the authentication key
    def get(self,name):
        """get request for an item"""
        item = ItemModel.find_by_name(name)
        if item :
            return item.json()
        return {"message": "item not found"},404


    def post(self,name):
        """psot request for an item"""
        if  ItemModel.find_by_name(name):
            return {"message":"an item with name {} already exists".format(name)},400 # bad request

        #calling the RequestParser to get the json
        data = Item.parser.parse_args()
        item = {'name':name,'price':data['price'],'store_id':data["store_id"]}
        item =ItemModel(**item)

        try :
            item.save_to_db()
        except :
            return {"message" : "an error occured when saving to the database."},500

        return item.json(),201


    def delete(self,name):
        """delete request for an item"""
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message":"item deleted"}
        else :
            return "an error occurred in the deletion processs"



    def put(self,name):
        """put[update] request for an item"""

        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)


        if item is None :
            item = ItemModel(name,data['price'],data['store_id'])
        else :
            item.price = data['price']

        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        """return all of the items in the database"""
        return {'all_items':[item.json() for item in ItemModel.query.all()]}
