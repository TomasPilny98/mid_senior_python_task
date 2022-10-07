from injector import singleton
from flask import jsonify
from flask_classful import FlaskView, route

from root.customer.customer_model import CustomerModel
from root.customer.customer_manager import CustomerManager
from root.order.order_manager import OrderManager
from root.rest.json_convertor import JsonConvertor
from root.main.dependency_injection_init import injector
from root.order.order_model import OrderModel


@singleton
class RestController(FlaskView):
    test_order_json = {
        "customerId": 1,
        "items": [
            {
                "itemId": 0,
                "itemName": "Car",
                "price": 100,
                "description": "awesome item"
            },
            {
                "itemId": 1,
                "itemName": "Car2",
                "price": 200,
                "description": "also awesome item"
            },
            {
                "itemId": 2,
                "itemName": "Car3",
                "price": 300,
                "description": "awesome item too"
            },
            {
                "itemId": 3,
                "itemName": "Car4",
                "price": 400,
                "description": "awesome item rly"
            }
        ]
    }

    test_person_customer_json = {
        "customerType": "person",
        "firstName": "Tomas",
        "lastName": "Pilny",
        "birthDate": "22/03/1998",
        "phoneNumber": 605768302,
        "emailAddress": "pilnytomas21@seznam.cz"
    }

    test_company_customer_json = {
        "customerType": "company",
        "ico": 54654654654,
        "dic": 21354654687,
        "phoneNumber": 605768302,
        "emailAddress": "pilnytomas21@seznam.cz"
    }

    @classmethod
    def initialization(cls):
        cls._customer_manager: CustomerManager = injector.get(CustomerManager)
        cls._order_manager: OrderManager = injector.get(OrderManager)
        cls._json_convertor: JsonConvertor = injector.get(JsonConvertor)

    @route('/create-customer', methods=['GET', 'POST'])
    def create_customer(self):
        # json_data: json = flask.request.json
        new_customer_model: CustomerModel = self._json_convertor.to_customer_model(self.test_person_customer_json)
        print(new_customer_model)
        new_customer_model: CustomerModel = self._json_convertor.to_customer_model(self.test_company_customer_json)
        print(new_customer_model)
        return jsonify(success=True)

    @route('/delete-customer', methods=['POST'])
    def delete_customer(self):
        pass

    @route('/get-all-customers-data', methods=['GET'])
    def delete_customer(self):
        pass

    @route('/create-order', methods=['GET', 'POST'])
    def create_order(self):
        new_order_model: OrderModel = self._json_convertor.to_order_model(self.test_order_json)
        print(new_order_model)
        return jsonify(success=True)

    @route('/delete-order', methods=['POST'])
    def delete_order(self):
        pass

    @route('/add-item', methods=['post'])
    def add_item(self):
        pass

    @route('/remove-item', methods=['post'])
    def remove_item(self):
        pass
