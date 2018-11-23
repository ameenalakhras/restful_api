from models.user import UserModel
from flask_restful import Resource,reqparse



class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('name',
    type=str,
    required = True,
    help="this field cannot be blank"
    )
    parser.add_argument('password',
    type=str,
    required = True,
    help="this field cannot be blank"
    )


    def post(self):
        """psot request for an user"""
        data = UserRegister.parser.parse_args()

        if  UserModel.find_by_name(data['name']):
            return {"message":"a user with name {} already exists".format(data['name'])},400 # bad request

        try :
            # it's like : UserModel(data['username'],data['password'])
            user = UserModel(**data)
            user.save_to_db()

        except :
            return {"message" : "and error occured when saving to the database."},500

        return user.json(),201


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
            item = ItemModel(name,data['price'])
        else :
            item.price = data['price']

        item.save_to_db()
        return item.json()



class UserList(Resource):
    def get(self):
        """return all of the users in the database"""
        return {'all_users':[user.json() for user in UserModel.query.all()]}
