from flask_restful import Resource
from flask import request
from DataModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema


class CustomerResource(Resource):

    def get(self, _id):
        customer = Customer.query.get_or_404(_id)
        return customer_schema.dump(customer)

    def delete(self, _id):
        customer = Customer.query.get_or_404(_id)
        db.session.delete(customer)
        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully deleted.', customer_schema.dump(customer)))

    def patch(self, _id):
        customer = Customer.query.get_or_404(_id)

        if 'name' in request.json:
            customer.name = request.json['name']
        if 'email' in request.json:
            customer.email = request.json['email']

        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully changed.', customer_schema.dump(customer)))

    def put(self, _id):
        customer = Customer.query.get_or_404(_id)
        customer.name = request.json['name']
        customer.email = request.json['email']
        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully updated.', customer_schema.dump(customer)))


