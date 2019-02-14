from flask_restful import Resource
from flask import jsonify

# Products View
class Products(Resource):
    def post(self):
        """Method to add a new product"""
        return jsonify({
            "message": "Product Added"
        })