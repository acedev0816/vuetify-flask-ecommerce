"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource, fields

from .security import require_auth
from . import api_rest


class SecureResource(Resource):
    """ Calls require_auth decorator on all requests """
    method_decorators = [require_auth]


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(Resource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):
    """ Unsecure Resource Class: Inherit from Resource """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

@api_rest.route('/test')
class Test(Resource):
    def get(self):
        return {'name': 'adsfadfadfadf'}


model_book = api_rest.model('Books', {
    'title' : fields.String('Title of the book.'),
    'id' : fields.Integer('id of the book.')
})

books = []
books.append({
    'title' : 'The Beetle Horde',
    'id' : 1
})

@api_rest.route('/books')
class Books(Resource):

    @api_rest.marshal_with(model_book, envelope='data')
    def get(self):
        return books

    @api_rest.expect(model_book)
    def post(self):
        new_book = api_rest.payload
        new_book['id'] = len(books) + 1
        books.append(new_book)
        return {'result' : 'book added'}, 201


