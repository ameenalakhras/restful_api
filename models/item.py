from db import db

class ItemModel(db.Model):

    __tablename__ = 'items' #SQLAlchemy tablename
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2)) # precision is the numbers after the dot in the float
    store_id = db.Column(db.Integer,db.ForeignKey('stores.id'))
    store = db.relationship("StoreModel")


    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        """returns a json representation of the data """
        return {"name":self.name,"price":self.price}

    @classmethod
    def find_by_name(cls,name):
        ### cls hers is like writing ItemModel
        return cls.query.filter_by(name=name).first() ## it's like : SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
