from flask import Flask
from .v1.views.product import Products
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

api.add_resource(Products, '/api/v1/products')