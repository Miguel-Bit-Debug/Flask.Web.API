from ..db.config_db import db

database = db

class Product(database.Model):
    __tablename__ = 'products'
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(200))
    description = database.Column(database.String(200))