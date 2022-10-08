from overrides import overrides
from injector import inject, singleton

from root.database.abstract.abstract_orders_repository import AbstractOrdersRepository
from root.database.manager.thread_session_request_manager import ThreadSessionRequestManager
from root.model.product_model import ProductModel
from root.model.order_model import OrderModel
from root.rest.parser.customer_json_parser import CustomerJsonParser


@singleton
class OrdersRepository(AbstractOrdersRepository):

    @inject
    def __init__(self, db_session: ThreadSessionRequestManager, json_convertor: CustomerJsonParser):
        self._db_session: ThreadSessionRequestManager = db_session
        self._json_convertor: CustomerJsonParser = json_convertor

    @overrides
    def add_order(self, customer_id: int, order_model: OrderModel) -> None:
        pass

    @overrides
    def remove_order(self, order_id: int) -> None:
        pass

    @overrides
    def add_item(self, order_id: int, item_model: ProductModel) -> None:
        pass

    @overrides
    def remove_item(self, order_id: int) -> None:
        pass

    @overrides
    def get_all_order_items(self, order_id: int) -> list[ProductModel]:
        pass


