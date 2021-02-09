from flask_restful import Resource
from flask import request
from sqlalchemy import text
from Validator import Validate
from CustomerModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import offset_limit, user_admin_check


class CustomersResource(Resource):
    # get all # admin
    def get(self):
        if user_admin_check() == 'admin':
            sort_by = request.args.get('sort_by', type=str)
            sort_type = request.args.get('sort_type', type=str)
            key = request.args.get('key', type=str)
            s = request.args.get('s', type=str)
            offset = request.args.get('offset', type=str)
            limit = request.args.get('limit', type=str)

            if sort_by is not None and sort_type is not None:
                name_type = sort_by + ' ' + sort_type
                customers = Customer.query.order_by(text(name_type)).all()
                elem_number = Customer.query.count()
            elif key is not None and s is not None:
                filter = key + ' like ' + '"%' + s + '%"'
                customers = Customer.query.filter(text(filter)).all()
                elem_number = len(customers)
            elif offset is not None and limit is not None and int(offset) >= 0:
                customers = offset_limit(offset, limit)
                print(type(customers))
                elem_number = customers.count()
            elif sort_by is None and sort_type is None and s is None and key is None and offset is None and limit is None:
                customers = Customer.query.all()
                elem_number = Customer.query.count()
            else:
                return response_schema.dump(Response(400, 'Not clear information.', "Error", 0))
            return response_schema.dump(Response(200, 'All Customers.', customers_schema.dump(customers), elem_number))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # create new
    def post(self):
        new_customer = Customer(
            name=request.json['name'],
            email=request.json['email'],
            user_id=None
        )
        validate = Validate(customer_schema.dump(new_customer)["name"], customer_schema.dump(new_customer)["email"])
        name, email, amount = Validate.main_valid(validate)
        if name is None:
            return response_schema.dump(Response(400, 'Name can only contain letters', "Error", 0))
        elif email is None:
            return response_schema.dump(Response(400, 'Email is not valid', "Error", 0))
        else:
            db.session.add(new_customer)
            db.session.commit()
            return response_schema.dump(Response(200, 'Customer has been successfully created.', customer_schema.dump(new_customer), 1))

