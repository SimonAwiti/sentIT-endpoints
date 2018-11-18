'''Creating app initializer'''
import os
from flask import Flask
from instance.config import app_config
from flask_jwt_extended import JWTManager

def create_app(config_name):
    '''creating  the app'''
 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.secret_key = os.getenv("SECRET_KEY")

    jwt = JWTManager(app)

    from app.version1.users.views import version1users_blueprints
    app.register_blueprint(version1users_blueprints)

    from app.version1.parcel_delivery_order.views import version1parcels_bp
    app.register_blueprint(version1parcels_bp)

    from app.version1.parcel_status.views import version1pstatus_bp
    app.register_blueprint(version1pstatus_bp)
    
    return app