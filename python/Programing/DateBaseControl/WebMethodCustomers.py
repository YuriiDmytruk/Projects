from flask_restful import Resource
from flask import request
from sqlalchemy import desc, asc, text
from Validator import Validate
from DataModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema


class CustomersResource(Resource):
    def get(self):
        name_type = request.args.get('sort_by', type=str) + ' ' + (request.args.get('sort_type', type=str))
        filter = request.args.get('sort_by', type=str) + ' like ' + '"%' + request.args.get('s', type=str) + '%"'
        customers = Customer.query.filter(text(filter)).order_by(text(name_type)).all()
        return customers_schema.dump(customers)

    def post(self):
        new_customer = Customer(
            name=request.json['name'],
            email=request.json['email']
        )
        validate = Validate(customer_schema.dump(new_customer)["name"], customer_schema.dump(new_customer)["email"])
        name, email = Validate.main_valid(validate)
        if name is None:
            return response_schema.dump(Response(400, 'Name can only contain letters'))
        elif email is None:
            return response_schema.dump(Response(400, 'Email is not valid'))
        else:
            db.session.add(new_customer)
            db.session.commit()
            return response_schema.dump(Response(200, 'Customer has been successfully created.', customer_schema.dump(new_customer)))




#customers = Customer.query.order_by(asc(Customer.name)).all()