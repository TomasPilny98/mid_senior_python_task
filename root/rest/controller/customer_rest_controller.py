import json

import flask
from injector import singleton
from flask import jsonify, Response
from flask_classful import FlaskView, route

from root.enum.json_data_enum import JsonDataEnum
from root.model.customer_model import CustomerModel
from root.manager.customer_manager import CustomerManager
from root.manager.order_manager import OrderManager
from root.rest.EnhancedJSONEncoder import EnhancedJSONEncoder
from root.rest.parser.customer_json_parser import CustomerJsonParser
from root.main.dependency_injection_init import injector


@singleton
class CustomerRestController(FlaskView):

    @classmethod
    def initialization(cls):
        cls._customer_manager: CustomerManager = injector.get(CustomerManager)
        cls._order_manager: OrderManager = injector.get(OrderManager)
        cls._json_convertor: CustomerJsonParser = injector.get(CustomerJsonParser)

    @route('/create-customer', methods=['GET', 'POST'])
    def create_customer(self) -> Response:
        json_data: json = flask.request.json
        new_customer: CustomerModel = self._json_convertor.to_customer_model(json_data)
        self._customer_manager.add_customer(new_customer)
        return jsonify(customer_created=True)

    @route('/delete-customer', methods=['GET', 'POST'])
    def delete_customer(self) -> Response:
        json_data: json = flask.request.json
        self._customer_manager.delete_customer(json_data[str(JsonDataEnum.CUSTOMER_ID)])
        return jsonify(customer_deleted=True)

    @route('/get-all-customers', methods=['GET'])
    def get_all_customers_data(self):
        all_customers: list[CustomerModel] = self._customer_manager.get_all_customers_data()
        return json.dumps(all_customers, cls=EnhancedJSONEncoder)



