from flask_restful import Resource
from flask import request
from Validator import Validate
from UserModel import User, Schema, dbu, user_schema, users_schema
from CustomerModel import Customer, Schema, db, customer_schema, customers_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import user_admin_check


class CustomerResource(Resource):
    # registration
    def post(self, _id):
        customer = Customer.query.get(_id)
        if customer is not None:
            if customer.user_id is None:
                password = request.json["password"]
                new_user = User(
                    name=customer.name,
                    email=customer.email,
                    password=password,
                    role="user",
                    login="0"
                )
                dbu.session.add(new_user)
                dbu.session.commit()
                _id = user_schema.dump(new_user)["id"]
                customer.user_id = _id
                db.session.commit()
                return response_schema.dump(Response(200, 'Customer was registered', user_schema.dump(new_user), 1))
            else:
                return response_schema.dump(Response(404, 'Customer is already registered', "Error", 0))
        else:
            return response_schema.dump(Response(404, 'Customer is not found', "Error", 0))

    # get by id # admin
    def get(self, _id):
        if user_admin_check() == 'admin':
            customer = Customer.query.get(_id)
            if customer is None:
                return response_schema.dump(Response(404, 'Customer is not found', "Error", 0))
            return response_schema.dump(Response(200, 'Customer with id:' + str(_id), customer_schema.dump(customer), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # delete # admin
    def delete(self, _id):
        if user_admin_check() == 'admin':
            customer = Customer.query.get(_id)
            if customer is None:
                return response_schema.dump(Response(404, 'Customer is not found', "Error", 0))
            db.session.delete(customer)
            db.session.commit()
            return response_schema.dump(Response(200, 'Customer has been successfully deleted.', customer_schema.dump(customer), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # change # admin
    def patch(self, _id):
        if user_admin_check() == 'admin':
            customer = Customer.query.get(_id)
            if customer is None:
                return response_schema.dump(Response(404, 'Customer is not found', "Error", 0))
            if 'name' in request.json:
                validate = Validate(request.json['name'], None)
                name, email, a = Validate.main_valid(validate)
                if name is None:
                    return response_schema.dump(Response(400, 'Name can only contain letters', "Error", 0))
                else:
                    customer.name = request.json['name']
            if 'email' in request.json:
                validate = Validate(None, request.json['email'])
                name, email, a = Validate.main_valid(validate)
                if email is None:
                    return response_schema.dump(Response(400, 'Email is not valid', "Error", 0))
                else:
                    customer.email = request.json['email']
            db.session.commit()
            return response_schema.dump(Response(200, 'Customer has been successfully changed.', customer_schema.dump(customer), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))
