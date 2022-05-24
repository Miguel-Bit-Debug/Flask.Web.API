from flask_marshmallow import Marshmallow
from ..models.product import Product

ma = Marshmallow()

def configure(app):
    ma.init_app(app)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True