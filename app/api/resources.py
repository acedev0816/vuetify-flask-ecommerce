"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Resource, fields

from .security import require_auth
from . import api_rest

import altair
from vega_datasets import data
cars = data.cars()


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


model_book = api_rest.model('Books', {
    'title' : fields.String('Title of the book.'),
    'author' : fields.String('Author of the book.')
})

books = [
    {'title': 'The Adventures of Huckleberry Finn', 'author': 'Mark Twain'},
    {'title': 'Frankenstein', 'author': 'Mary Shelley'},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
    {'title': 'The Little Prince', 'author': 'Antoine de Saint-Exupéry'},
    {'title': 'The Color Purple', 'author': 'Alice Walker'},
    {'title': 'Little Women', 'author': 'Louisa May Alcott'},
    {'title': 'Great Expectations', 'author': 'Charles Dickens'},
    {'title': 'The Scarlet Letter', 'author': 'Nathaniel Hawthorne'},
    {'title': 'Gone with the Wind', 'author': 'Margaret Mitchell'},
    {'title': 'The Picture of Dorian Gray', 'author': 'Oscar Wilde'},
    {'title': 'The Metamorphosis', 'author': 'Franz Kafka'}
]


@api_rest.route('/books')
class Books(Resource):

    @api_rest.marshal_with(model_book, envelope='data')
    def get(self):
        return books

    # @api_rest.expect(model_book)
    # def post(self):
    #     new_book = api_rest.payload
    #     new_book['id'] = len(books) + 1
    #     books.append(new_book)
    #     return {'result' : 'book added'}, 201

@api_rest.route('/vega_cars')
class VegaCars(Resource):

    def get(self):
        chart = altair.Chart(cars).mark_point().encode(
            x='Horsepower',
            y='Miles_per_Gallon',
            color='Origin'
        ).interactive()
        return chart.to_dict()
