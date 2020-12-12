from flask_restful import Resource
from UserModel import User, Schema, dbu, user_schema, users_schema
from ResponseModel import Response, response_schema
from flask import request


class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    # logout
    def put(self):
        users = User.query.all()
        check = 0
        x = 0
        while check < len(users_schema.dump(users)):
            if users_schema.dump(users)[check]["login"] == 1:
                x = 1
                _i = users_schema.dump(users)[check]["id"]
                user = User.query.get(_i)
                user.login = 0
                dbu.session.commit()
            check += 1
        if x == 1:
            return response_schema.dump(Response(200, 'User was Logout'))
        else:
            return response_schema.dump(Response(400, 'No Users is login'))

    # login
    def post(self):
        users = User.query.all()
        y = 0
        check = 0
        while check < len(users_schema.dump(users)):
            if users_schema.dump(users)[check]["login"] == 1:
                y = 1
                break
            check += 1
        if y == 1:
            return response_schema.dump(Response(400, 'Firstly you should logout'))
        else:
            email = request.json['email']
            password = request.json['password']
            x = 0
            check = 0
            while check < len(users_schema.dump(users)):
                if users_schema.dump(users)[check]["email"] == email:
                    x = 1
                    if users_schema.dump(users)[check]["password"] == password:
                        _i = users_schema.dump(users)[check]["id"]
                        user = User.query.get(_i)
                        user.login = 1
                        dbu.session.commit()
                        return response_schema.dump(Response(200, "User was Login"))
                    else:
                       return response_schema.dump(Response(400, 'Wrong Password'))
                check += 1
            if x == 0:
                return response_schema.dump(Response(400, 'User with this email was not found'))