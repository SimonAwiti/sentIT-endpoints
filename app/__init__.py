'''Creating app initializer'''
import os
from flask import Flask
from instance.config import configuration

def create_app(config):
    '''creating  the app'''
 
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(configuration[config]) finish the configs
    app.secret_key = os.getenv("SECRET_KEY")

    from app.version1.users.views import version1users_blueprints
    app.register_blueprint(version1users_blueprints)

    from app.version1.parcel_delivery_order.views import version1parcels_bp
    app.register_blueprint(version1parcels_bp)

    return app