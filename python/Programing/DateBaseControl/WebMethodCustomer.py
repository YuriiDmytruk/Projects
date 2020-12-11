from flask_restful import Resource
from flask import request
from Validator import Validate
from DataModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema


class CustomerResource(Resource):

    def get(self, _id):
        customer = Customer.query.get(_id)
        if customer is None:
            return response_schema.dump(Response(404, 'Customer is not found'))
        return customer_schema.dump(customer)

    def delete(self, _id):
        customer = Customer.query.get(_id)
        if customer is None:
            return response_schema.dump(Response(404, 'Customer is not found'))
        db.session.delete(customer)
        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully deleted.', customer_schema.dump(customer)))

    def patch(self, _id):
        customer = Customer.query.get(_id)
        if customer is None:
            return response_schema.dump(Response(404, 'Customer is not found'))
        if 'name' in request.json:
            validate = Validate(request.json['name'], None)
            name, email = Validate.main_valid(validate)
            if name is None:
                return response_schema.dump(Response(400, 'Name can only contain letters'))
            else:
                customer.name = request.json['name']
        if 'email' in request.json:
            validate = Validate(None, request.json['email'])
            name, email = Validate.main_valid(validate)
            if email is None:
                return response_schema.dump(Response(400, 'Email is not valid'))
            else:
                customer.email = request.json['email']
        db.session.commit()
        return response_schema.dump(Response(200, 'Customer has been successfully changed.', customer_schema.dump(customer)))

    def put(self, _id):
        customer = Customer.query.get(_id)
        if customer is None:
            return response_schema.dump(Response(404, 'Customer is not found'))
        validate = Validate(request.json['name'], request.json['email'])
        name, email = Validate.main_valid(validate)
        if name is None:
            return response_schema.dump(Response(400, 'Name can only contain letters'))
        elif email is None:
            return response_schema.dump(Response(400, 'Email is not valid'))
        else:
            customer.name = request.json['name']
            customer.email = request.json['email']
            db.session.commit()
            return response_schema.dump(Response(200, 'Customer has been successfully updated.', customer_schema.dump(customer)))


