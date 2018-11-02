'''Creating app initializer'''
import os
from flask import Flask
from instance.config import configuration

def create_app(config):
    '''creating  the app'''
 
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_object(configuration[config]) finish the configs
    app.secret_key = os.getenv("SECRET_KEY")

    return app