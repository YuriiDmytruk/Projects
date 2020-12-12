from flask_restful import Api
from AppConfig import app
from WebMethodInit import InitResource
from WebMethodCustomers import CustomersResource
from WebMethodUtil import UtilResource
from WebMethodUsers import UsersResource
from WebMethodUser import UserResource

"""
Make 1 class User; in diferent methods make login, logout, registration,
add to UserSchema 1 field is_in to know if user is in also add admin by name Admin
who can check all users
"""


api = Api(app)

api.add_resource(UtilResource, '/create')
api.add_resource(InitResource, '/init')
api.add_resource(CustomersResource, '/customers')
api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/user/<int:_id>')




if __name__ == '__main__':
    app.run(debug=True)
