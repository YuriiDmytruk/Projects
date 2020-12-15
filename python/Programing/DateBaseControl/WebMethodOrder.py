from flask_restful import Resource
from flask import request
from OrderModel import Order, Schema, dbo, order_schema, orders_schema
from ProductModel import Product, Schema, dbp, product_schema, products_schema
from ResponseModel import Response, response_schema
from Validator import Validate
from WebMethodUtil import user_admin_check


class OrderResource(Resource):
    # get by id # admin
    def get(self, _id):
        if user_admin_check() == 'admin':
            order = Order.query.get(_id)
            if order is None:
                return response_schema.dump(Response(404, 'Order is not found', "Error", 0))
            return response_schema.dump(Response(200, 'Order with id:' + str(_id), order_schema.dump(order), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # delete # admin
    def delete(self, _id):
        if user_admin_check() == 'admin':
            order = Order.query.get(_id)
            if order is None:
                return response_schema.dump(Response(404, 'Order is not found', "Error", 0))
            else:
                dbo.session.delete(order)
                dbo.session.commit()
                return response_schema.dump(Response(200, 'Order has been successfully deleted.', order_schema.dump(order), 0))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # change # admin
    def patch(self, _id):
        if user_admin_check() == 'admin':
            order = Order.query.get(_id)
            if order is None:
                return response_schema.dump(Response(404, 'Order is not found', "Error", 0))
            if 'amount' in request.json:
                validate = Validate(None, None, request.json['amount'])
                name, email, amount = Validate.main_valid(validate)
                if amount is None:
                    return response_schema.dump(Response(400, 'Name can only contain letters', "Error", 0))
                else:
                    product = Product.query.get(int(order_schema.dump(order)["product_id"]))
                    if int(amount) + order.amount < product.amount:
                        order.name = request.json['amount']
                        dbo.session.commit()
                        return response_schema.dump(Response(200, 'Order has been successfully changed.', order_schema.dump(order), 1))
                    else:
                        return response_schema.dump(Response(400, 'You need more then we have', "Error", 0))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))
