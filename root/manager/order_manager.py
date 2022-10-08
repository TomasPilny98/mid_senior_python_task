from injector import singleton, inject
from overrides import overrides

from root.database.abstract.abstract_orders_repository import AbstractOrdersRepository
from root.database.repository.orders_repository import OrdersRepository
from root.model.product_model import ProductModel
from root.model.order_model import OrderModel


@singleton
class OrderManager(AbstractOrdersRepository):

    @inject
    def __init__(self, orders_repository: OrdersRepository):
        self._orders_repository: OrdersRepository = orders_repository

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

