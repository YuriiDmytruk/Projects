from flask_restful import Resource
from flask import request
from DataModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema


class CustomersResource(Resource):
    def get(self):
        customers = Customer.query.all()
        return customers_schema.dump(customers)

    def post(self):
        new_customer = Customer(
            name=request.json['name'],
            email=request.json['email']
        )
        db.session.add(new_customer)
        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully created.', customer_schema.dump(new_customer)))




