from flask_restful import Resource
from UserModel import User, Schema, dbu, user_schema, users_schema
from ResponseModel import Response, response_schema
from CustomerModel import Customer, Schema, db, customer_schema, customers_schema
from flask import request


class UserResource(Resource):
    def get(self, _id):
        user = User.query.get(_id)
        return user_schema.dump(user)

    # register
    def post(self, _id):
        customer = Customer.query.get(_id)
        if customer is None or customer.registered == 1:
            return response_schema.dump(Response(404, 'You cant login this customer'))
        else:
            email = customer_schema.dump(customer)["email"]
            new_user = User(
                first_name=request.json['first_name'],
                last_name=request.json['last_name'],
                email=email,
                password=request.json['password'],
                login=0
            )
            db.session.add(new_user)
            db.session.commit()
            customer.user_id = user_schema.dump(new_user)["id"]
            customer.registered = 1
            db.session.commit()
            return response_schema.dump(Response(200, 'User has been successfully registered.'))





