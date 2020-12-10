from flask_restful import Resource

from DataModel import Customer, db


class UtilResource(Resource):
    def get(self):
        name = "Name"
        email = "Email"
        check = 0
        while check < 5:
            new_post = Customer(
                name=name,
                email=email
            )
            db.session.add(new_post)
            check += 1
        db.session.commit()
        return '5 Test Customers was successfully created', 200
