from flask import Flask
from flask_cors import CORS
from root.rest.controller.customer_rest_controller import CustomerRestController
from root.rest.controller.order_rest_controller import OrderRestController
from root.rest.controller.product_rest_controller import ProductRestController


class FlaskInitializer:

    def __init__(self):
        self._app: Flask = Flask(__name__)
        self._app.config['CORS_HEADERS'] = 'Content-type'
        # don't store secret_key like this in production, this is for development purpose only
        self._app.config['SECRET_KEY'] = '/xa1/xb4/x02,Rg/x89L/x19/xaab/xf5'
        self.init_rest_controller()
        CORS(self._app)

    @property
    def app_instance(self):
        return self._app

    def init_rest_controller(self):
        CustomerRestController.initialization()
        CustomerRestController.register(self._app, route_base='/', route_prefix='api/customer')
        OrderRestController.initialization()
        OrderRestController.register(self._app, route_base='/', route_prefix='api/order')
        ProductRestController.initialization()
        ProductRestController.register(self._app, route_base='/', route_prefix='api/product')

