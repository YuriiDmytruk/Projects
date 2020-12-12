from flask_restful import Resource
from CustomerModel import db
from UserModel import dbu


class InitResource(Resource):
    def get(self):

        dbu.drop_all()
        dbu.create_all()
        db.drop_all()
        db.create_all()
        return 'DB Created', 200
