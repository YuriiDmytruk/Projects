from flask_restful import Resource
from DataModel import db

class InitResource(Resource):
    def get(self):
        db.drop_all()
        db.create_all()
        return 'DB Created', 200
