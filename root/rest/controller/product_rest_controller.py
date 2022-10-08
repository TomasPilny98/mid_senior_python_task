
from injector import singleton
from flask_classful import FlaskView, route


from root.manager.customer_manager import CustomerManager
from root.manager.order_manager import OrderManager
from root.rest.parser.customer_json_parser import CustomerJsonParser
from root.main.dependency_injection_init import injector


@singleton
class ProductRestController(FlaskView):

    @classmethod
    def initialization(cls):
        cls._customer_manager: CustomerManager = injector.get(CustomerManager)
        cls._order_manager: OrderManager = injector.get(OrderManager)
        cls._json_convertor: CustomerJsonParser = injector.get(CustomerJsonParser)

    @route('/create-product', methods=['post'])
    def create_product(self):
        pass

    @route('/delete-product', methods=['POST'])
    def delete_product(self):
        pass

    @route('/update-product', methods=['post'])
    def update_product(self):
        pass
