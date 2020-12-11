from flask_restful import Resource

from DataModel import Customer, db


class UtilResource(Resource):
    def get(self):
        name = ["Yurii", "Roma", "Bob", "Tom", "Ann"]
        email = "Email"
        check = 0
        while check < len(name):
            new_post = Customer(
                name=name[check],
                email=email
            )
            db.session.add(new_post)
            check += 1
        db.session.commit()
        return '5 Test Customers was successfully created', 200
