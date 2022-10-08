import json

import flask
from injector import singleton
from flask import jsonify
from flask_classful import FlaskView, route

from root.manager.customer_manager import CustomerManager
from root.manager.order_manager import OrderManager
from root.rest.parser.customer_json_parser import CustomerJsonParser
from root.main.dependency_injection_init import injector
from root.model.order_model import OrderModel


@singleton
class OrderRestController(FlaskView):

    @classmethod
    def initialization(cls):
        cls._customer_manager: CustomerManager = injector.get(CustomerManager)
        cls._order_manager: OrderManager = injector.get(OrderManager)
        cls._json_convertor: CustomerJsonParser = injector.get(CustomerJsonParser)

    @route('/create-order', methods=['GET', 'POST'])
    def create_order(self):
        json_data: json = flask.request.json
        new_order_model: OrderModel = self._json_convertor.to_order_model(json_data)
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
