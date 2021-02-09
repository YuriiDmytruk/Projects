from flask_restful import Resource
from flask import request
from sqlalchemy import text
from OrderModel import Order, Schema, dbo, order_schema, orders_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import offset_limit, user_admin_check, login_check


class OrdersResource(Resource):
    # get all # login self # admin
    def get(self):
        if login_check() is not None:
            sort_by = request.args.get('sort_by', type=str)
            sort_type = request.args.get('sort_type', type=str)
            key = request.args.get('key', type=str)
            s = request.args.get('s', type=str)
            offset = request.args.get('offset', type=str)
            limit = request.args.get('limit', type=str)

            if sort_by is not None and sort_type is not None:
                name_type = sort_by + ' ' + sort_type
                orders = Order.query.order_by(text(name_type)).all()
            elif key is not None and s is not None:
                filter = key + ' like ' + '"%' + s + '%"'
                orders = Order.query.filter(text(filter)).all()
            elif offset is not None and limit is not None and int(offset) >= 0:
                orders = offset_limit(offset, limit)
            elif sort_by is None and sort_type is None and s is None and key is None and offset is None and limit is None:
                orders = Order.query.all()
            else:
                return response_schema.dump(Response(400, 'Not clear information.', "Error", 0))
            if user_admin_check() == "admin":
                elem_number = len(orders)
                return response_schema.dump(Response(200, 'All Orders.', orders_schema.dump(orders), elem_number))
            else:
                login_id = login_check()
                user_orders = []
                check = 0
                while check < len(orders_schema.dump(orders)):
                    if orders_schema.dump(orders)[check]["user_id"] == login_id:
                        user_orders.append(orders_schema.dump(orders)[check])
                    check += 1
                print(user_orders)
                return response_schema.dump(Response(200, 'Your Orders', user_orders, len(user_orders)))
        else:
            return response_schema.dump(Response(401, 'Unauthorized user.', "Error", 0))
