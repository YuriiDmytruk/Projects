from flask_restful import Resource
from flask import request
from sqlalchemy import text
from Validator import Validate
from ProductModel import Product, Schema, dbp, product_schema, products_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import offset_limit, user_admin_check, login_check


class ProductsResource(Resource):
    # get all # login
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
                customers = Product.query.order_by(text(name_type)).all()
                elem_number = Product.query.count()
            elif key is not None and s is not None:
                filter = key + ' like ' + '"%' + s + '%"'
                customers = Product.query.filter(text(filter)).all()
                elem_number = len(customers)
            elif offset is not None and limit is not None and int(offset) >= 0:
                customers = offset_limit(offset, limit)
                print(type(customers))
                elem_number = customers.count()
            elif sort_by is None and sort_type is None and s is None and key is None and offset is None and limit is None:
                customers = Product.query.all()
                elem_number = Product.query.count()
            else:
                return response_schema.dump(Response(400, 'Not clear information.', "Error", 0))
            return response_schema.dump(Response(200, 'All products.', products_schema.dump(customers), elem_number))
        else:
            return response_schema.dump(Response(401, 'Unauthorized user.', "Error", 0))

    # add new # admin
    def post(self):
        if user_admin_check() == 'admin':
            new_product = Product(
                name=request.json['name'],
                amount=request.json['amount']
            )
            validate = Validate(product_schema.dump(new_product)["name"], None,  product_schema.dump(new_product)["amount"])
            name, email, amount = Validate.main_valid(validate)
            if name is None:
                return response_schema.dump(Response(400, 'Name can only contain letters', "Error", 0))
            elif amount is None:
                return response_schema.dump(Response(400, 'Amount is not valid', "Error", 0))
            else:
                dbp.session.add(new_product)
                dbp.session.commit()
                elem_number = 1
                return response_schema.dump(
                    Response(200, 'Product has been successfully created.', product_schema.dump(new_product), elem_number))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))
