from flask_restful import Api
from AppConfig import app

from WebMethodInit import InitResource
from WebMethodUtil import UtilResource

from WebMethodUser import UserResource
from WebMethodUsers import UsersResource

from WebMethodCustomer import CustomerResource
from WebMethodCustomers import CustomersResource

from WebMethodProducts import ProductsResource
from WebMethodProduct import ProductResource

from WebMethodOrder import OrderResource
from WebMethodOrders import OrdersResource

api = Api(app)

api.add_resource(InitResource, '/init')
api.add_resource(UtilResource, '/create')

api.add_resource(CustomerResource, '/customer/<int:_id>')
api.add_resource(CustomersResource, '/customers')

api.add_resource(UserResource, '/user/<int:_id>')
api.add_resource(UsersResource, '/users')

api.add_resource(ProductResource, '/product/<int:_id>')
api.add_resource(ProductsResource, '/products')

api.add_resource(OrderResource, '/order/<int:_id>')
api.add_resource(OrdersResource, '/orders')



if __name__ == '__main__':
    app.run(debug=True)
