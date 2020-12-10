from flask_restful import Api

from AppConfig import app
from WebMethodInit import InitResource
from WebMethodCustomer import CustomerResource
from WebMethodCustomers import CustomersResource
from WebMethodUtil import UtilResource

api = Api(app)

api.add_resource(InitResource, '/init')
api.add_resource(CustomerResource, '/customer/<int:_id>')
api.add_resource(CustomersResource, '/customers')
api.add_resource(UtilResource, '/create')


if __name__ == '__main__':
    app.run(debug=True)
