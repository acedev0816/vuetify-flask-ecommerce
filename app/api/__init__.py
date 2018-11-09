""" API Blueprint Application """

from flask import Blueprint, current_app
from flask_restplus import Api

api_bp = Blueprint('api_bp', __name__, url_prefix='/api')  #/api is the new endpoint
api_rest = Api(api_bp, version='1.0', doc='/doc')  # doc=False to turn off SwaggerUI

@api_bp.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response


# Import resources to ensure view is registered
from .resources import * # NOQA
