from ..models.product import Product
from ..db import config_db

class ProductRepository:
    def __init__(self):
        self.product = Product()
        self.db = config_db.db

    def listProduct(self):
        return self.product.query.all()

    def addProduct(self, product):
        if product != '':
            self.db.session.add(product)
            self.db.session.commit()
            return True
        return False
    
    def getById(self, id):
        return self.product.query.filter_by(id=id)

    def updateProduct(self, id, product):
        oldProduct = self.product.query.filter_by(id=id)
        oldProduct.update(product)
        self.db.session.commit()

    def deleteProduct(self, id):
        self.product.query.filter_by(id=id).delete()
        self.db.session.commit()