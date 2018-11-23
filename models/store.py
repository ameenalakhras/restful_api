from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores' #SQLAlchemy tablename
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    # just telling the db that there's a relationship between ItemModel and StoreModel will make it understand it (because we told it who is the Foreignkey in ItemModel)
    # lazy=dynamic : prevents making an object for every single item[it will make creating an item alot faster but calling items slower]; you have to use .all() when calling them like in (json funciton)
    items = db.relationship("ItemModel",lazy="dynamic")

    def __init__(self,name):
        self.name = name

    def json(self):
        """returns a json representation of the data """
        return {"name":self.name,"items":[item.json() for item in self.items.all()]}

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
