from flask_restful import Resource
from flask import request
from sqlalchemy import text
from UserModel import User, Schema, dbu, user_schema, users_schema
from ResponseModel import Response, response_schema
from WebMethodUtil import login_check, offset_limit, user_admin_check


class UsersResource(Resource):

    # get all # admin
    def get(self):
        if user_admin_check() == 'admin':
            sort_by = request.args.get('sort_by', type=str)
            sort_type = request.args.get('sort_type', type=str)
            key = request.args.get('key', type=str)
            s = request.args.get('s', type=str)
            offset = request.args.get('offset', type=str)
            limit = request.args.get('limit', type=str)

            if sort_by is not None and sort_type is not None:
                name_type = sort_by + ' ' + sort_type
                users = User.query.order_by(text(name_type)).all()
                elem_number = User.query.count()
            elif key is not None and s is not None:
                filter = key + ' like ' + '"%' + s + '%"'
                users = User.query.filter(text(filter)).all()
                elem_number = len(users)
            elif offset is not None and limit is not None and int(offset) >= 0:
                users = offset_limit(offset, limit)
                elem_number = users.count()
            elif sort_by is None and sort_type is None and s is None and key is None and offset is None and limit is None:
                users = User.query.all()
                elem_number = User.query.count()
            else:
                return response_schema.dump(Response(400, 'Not clear information.', "Error", 0))
            return response_schema.dump(Response(200, 'All Users.', users_schema.dump(users), elem_number))
        else:
            return response_schema.dump(Response(403, 'Requested resource is forbidden', "Error", 0))

    # login
    def post(self):
        if login_check() is None:
            email = request.json['email']
            password = request.json['password']
            users = User.query.all()
            user = None
            if email is not None:
                check = 0
                while check < len(users_schema.dump(users)):
                    if email == users_schema.dump(users)[check]["email"]:
                        _id = users_schema.dump(users)[check]["id"]
                        user = User.query.get(_id)
                        break
                    check += 1
            else:
                return response_schema.dump(Response(400, 'No Email', "Error", 0))
            if user is not None:
                if user_schema.dump(user)["password"] == password:
                    user.login = "1"
                    dbu.session.commit()
                    return response_schema.dump(Response(200, 'User Login', user_schema.dump(user), 1))
                else:
                    return response_schema.dump(Response(400, 'Wrong Password', "Error", 0))
            else:
                return response_schema.dump(Response(400, 'Wrong Email', "Error", 0))
        else:
            return response_schema.dump(Response(400, 'Logout from other acc', "Error", 0))

    # logout
    def put(self):
        if login_check() is None:
            return response_schema.dump(Response(400, 'No Users login', "Error", 0))
        else:
            _id = login_check()
            user = User.query.get(_id)
            if user is not None:
                user.login = "0"
                dbu.session.commit()
                return response_schema.dump(Response(200, 'User Logout', user_schema.dump(user), 1))
            else:
                return response_schema.dump(Response(404, 'No Users find', "Error", 0))
