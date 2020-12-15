from flask_restful import Resource
from UserModel import User, Schema, dbu, user_schema, users_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import user_admin_check


class UserResource(Resource):
    # get by ID # admin
    def get(self, _id):
        if user_admin_check() == 'admin':
            user = User.query.get(_id)
            if user is None:
                return response_schema.dump(Response(404, 'User is not found', "Error", 0))
            return response_schema.dump(Response(200, 'User with id:' + str(_id), user_schema.dump(user), 1))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))
