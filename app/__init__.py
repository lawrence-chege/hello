"""
    This module cnfigures how the app will run
"""
import datetime
from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from instance.config import config
from app.api.v1 import version_one as v1
from migrations import DbModel
from app.api.v1.models.users import RevokedTokenModel


timeout = datetime.timedelta(hours=12)

def create_app(config_name):
    """
        This function creates a flask app and
        registers api version blueprints 
    """
    
    APP = Flask(__name__, instance_relative_config=True)
    APP.config.from_object(config[config_name])
    CORS(APP)
    JWTManager(APP)
    APP.register_blueprint(v1)
    APP.config['JWT_ACCESS_TOKEN_EXPIRES'] = timeout
    APP.config['JWT_SECRET_KEY'] = '123rfgbrf776yt'
    APP.url_map.strict_slashes = False
    
    return APP