from flask import Flask
from flask_migrate import Migrate
from .routes.product import bp_product
from .db.config_db import configure as config_db
from .serialize.productSchema import configure as config_ma

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    config_db(app)
    config_ma(app)

    Migrate(app, app.db)
    
    app.register_blueprint(bp_product)
    
    return app
