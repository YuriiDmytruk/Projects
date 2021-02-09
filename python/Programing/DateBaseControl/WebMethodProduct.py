from flask_restful import Resource
from datetime import datetime
from flask import request
from Validator import Validate
from ProductModel import Product, Schema, dbp, product_schema, products_schema
from UserModel import User, Schema, dbu, user_schema, users_schema
from OrderModel import Order, Schema, dbo, order_schema, orders_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import login_check, user_admin_check


class ProductResource(Resource):
    # get by ID # login
    def get(self, _id):
        if login_check() is not None:
            product = Product.query.get(_id)
            if product is None:
                return response_schema.dump(Response(404, 'Product is not found', "Error", 0))
            else:
                return response_schema.dump(Response(200, 'Product with id:' + str(_id), product_schema.dump(product), 0))
        else:
            return response_schema.dump(Response(401, 'Unauthorized user.', "Error", 0))

    # delete # admin
    def delete(self, _id):
        if user_admin_check() == 'admin':
            product = Product.query.get(_id)
            if product is None:
                return response_schema.dump(Response(404, 'Product is not found', "Error", 0))
            dbp.session.delete(product)
            dbp.session.commit()
            return response_schema.dump(Response(200, 'Product has been successfully deleted.', product_schema.dump(product), 0))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # change # admin
    def patch(self, _id):
        if user_admin_check() == 'admin':
            product = Product.query.get(_id)
            if product is None:
                return response_schema.dump(Response(404, 'Product is not found', "Error", 0))
            if 'name' in request.json:
                validate = Validate(request.json['name'], None, None)
                name, email, amount = Validate.main_valid(validate)
                if name is None:
                    return response_schema.dump(Response(400, 'Name can only contain letters', "Error", 0))
                else:
                    product.name = request.json['name']
            if 'amount' in request.json:
                validate = Validate(None, None,  request.json['amount'])
                name, email, amount = Validate.main_valid(validate)
                if amount is None:
                    return response_schema.dump(Response(400, 'Amount is not valid', "Error", 0))
                else:
                    product.amount = request.json['amount']
            dbp.session.commit()
            return response_schema.dump(Response(200, 'Product has been successfully changed.', product_schema.dump(product), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # buy # login
    def put(self, _id):
        if login_check() is not None:
            amount = request.json["amount"]
            i_d = login_check()
            if i_d is not None:
                user = User.query.get(i_d)
                if amount is not None:
                    product = Product.query.get(_id)
                    if product is not None:
                        if amount is not None:
                            amount = int(amount)
                            if product.amount >= amount:
                                date = datetime.now()
                                current_time = date.strftime("%H:%M:%S")
                                print("Current Time =", current_time)
                                product.amount -= amount
                                new_order = Order(
                                    user_id=user.id,
                                    product_id=product.id,
                                    amount=amount,
                                    date=date
                                )
                                dbo.session.add(new_order)
                                dbp.session.commit()
                                dbo.session.commit()
                                return response_schema.dump(Response(200, 'New Order add', order_schema.dump(new_order), 1))
                            else:
                                return response_schema.dump(Response(400, 'You need more then we have', "Error", 0))
                        else:
                            return response_schema.dump(Response(400, 'Amount must be int', "Error", 0))
                    else:
                        return response_schema.dump(Response(400, 'Products with id: ' + _id + ', do not exist', "Error", 0))
                else:
                    return response_schema.dump(Response(400, 'None name or amount', "Error", 0))
            else:
                return response_schema.dump(Response(400, 'You should login', "Error", 0))
        else:
            return response_schema.dump(Response(401, 'Unauthorized user.', "Error", 0))







