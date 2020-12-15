from flask_restful import Resource
from ResponseModel import Response, response_schema
from CustomerModel import Customer, Schema, db, customer_schema, customers_schema
from OrderModel import Order, Schema, dbo, order_schema, orders_schema
from UserModel import User, Schema, dbu, user_schema, users_schema
from UserModel import User, dbu


class UtilResource(Resource):
    def get(self):
        name = "Name"
        email = "Email"
        check = 0
        while check < 3:
            new_post = Customer(
                name=name + str(check),
                email=email + str(check),
                user_id=None
            )
            db.session.add(new_post)
            check += 1
        db.session.commit()

        name = "Name"
        email = "Email"
        check = 0
        while check < 3:
            new_post = User(
                name=name + str(check),
                email=email + str(check),
                password="01234",
                role="user",
                login="0"
            )
            dbu.session.add(new_post)
            check += 1
        dbu.session.commit()

        check = 0
        while check < 2:
            new_post = Order(
                user_id="1",
                product_id="1",
                amount="5",
                date=None

            )
            dbo.session.add(new_post)
            check += 1
        neww_post = Order(
            user_id="3",
            product_id="1",
            amount="5",
            date=None

        )
        dbo.session.add(neww_post)
        dbo.session.commit()
        customers = Customer.query.all()
        users = User.query.all()
        return response_schema.dump(Response(200, 'Test Customers was successfully created', customers_schema.dump(customers), users_schema.dump(users)))



def offset_limit(offset, limit):
    limit = int(limit)
    offset = limit * int(offset)
    print(limit, offset)
    customers = Customer.query.offset(offset).limit(limit)
    return customers


def user_admin_check():
    role = None
    _id = login_check()
    if _id is None:
        return None
    else:
        user = User.query.get(_id)
        role = user_schema.dump(user)["role"]
    return role


def login_check():
    check = 0
    users = User.query.all()
    _id = None
    while check < len(users_schema.dump(users)):
        if users_schema.dump(users)[check]["login"] == "1":
            _id = users_schema.dump(users)[check]["id"]
            break
        check += 1
    return _id
