from injector import singleton
import flask
from flask import json, jsonify
from flask_classful import FlaskView, route

from root.customer.customer_model import CustomerModel
from root.manager.customer_manager import CustomerManager
from root.manager.order_manager import OrderManager
from root.json_convertor import JsonConvertor
from root.main.dependency_injection_init import injector
from root.order.order_model import OrderModel


@singleton
class RestController(FlaskView):
    test_order_json = {
        "items": [
            {
                "itemId": 0,
                "price": 100,
                "description": "awesome item"
            },
            {
                "itemId": 1,
                "price": 200,
                "description": "also awesome item"
            },
            {
                "itemId": 2,
                "price": 300,
                "description": "awesome item too"
            },
            {
                "itemId": 3,
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

    @route('/delete-customer', methods=['DELETE'])
    def delete_customer(self):
        pass

    @route('/create-order', methods=['POST'])
    def create_order(self):
        json_data: json = flask.request.json
        new_order_model: OrderModel = self._json_convertor.to_order_model(self.test_order_json)  # json_data
        return jsonify(success=True)

    @route('/delete-order', methods=['DELETE'])
    def delete_order(self):
        pass

    @route('/update-order', methods=['POST'])
    def update_order(self):
        pass

    @route('/get-all-customers', methods=['GET'])
    def get_all_customers(self):
        pass
