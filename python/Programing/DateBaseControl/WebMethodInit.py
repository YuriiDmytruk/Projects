from flask_restful import Resource
from CustomerModel import db
from UserModel import dbu, User
from ProductModel import dbp, Product
from OrderModel import dbo


class InitResource(Resource):
    def get(self):
        db.drop_all()
        dbu.drop_all()
        dbp.drop_all()
        dbo.drop_all()
        db.create_all()
        dbo.create_all()
        dbu.create_all()
        dbp.create_all()

        new_post = User(
            name="Admin",
            email="admin@gmail.com",
            password="0admin0",
            role="admin",
            login="0",
        )
        dbu.session.add(new_post)
        dbu.session.commit()

        name = ["Mango", "Apple", "Orange", "Pineapple", "Watermelon"]
        amount = [34, 12, 34, 67, 12]
        check = 0
        while check < len(name):
            new_post = Product(
                name=name[check],
                amount=amount[check]
            )
            dbp.session.add(new_post)
            check += 1
        dbp.session.commit()

        return 'DB Created', 200
