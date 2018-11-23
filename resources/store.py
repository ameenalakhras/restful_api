from flask_restful import Resource,reqparse
from models.store import StoreModel

class Store(Resource):

    def get(self,name):
        store = StoreModel.find_by_name(name)

        if store is not None :
            return store.json()
        else :
            return {"message":"Store doesn't exist ! "},404

    def post(self,name):
        store = StoreModel.find_by_name(name)
        if StoreModel.find_by_name(name):
            return {"message":"Store already exitsts"}

        store = StoreModel(name)
        try :
            store.save_to_db()
        except :
            return {"message":"a problem has occured saving store to db"}

        return store.json(),201

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store :
            try :
                store.delete_from_db()
                return {"message":"the store has been deleted successfully"}
            except :
                return {"message":"a problem happened while deleting from databse "}
        return {"message":"Store doesn't exist!"}


class StoreList(Resource):
    def get(self):
        "return all of the stores from the database"
        return {'all_stores':[store.json() for store in StoreModel.query.all()]}
