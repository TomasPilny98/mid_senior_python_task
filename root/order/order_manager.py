from injector import singleton
from overrides import overrides

from root.database.abstract.abstract_orders_repository import AbstractOrdersRepository
from root.item.item_model import ItemModel
from root.order.order import OrderModel


@singleton
class OrderManager(AbstractOrdersRepository):
    @overrides
    def add_order(self, customer_id: int, order_model: OrderModel) -> None:
        pass

    @overrides
    def remove_order(self, order_id: int) -> None:
        pass

    @overrides
    def add_item(self, order_id: int, item_model: ItemModel) -> None:
        pass

    @overrides
    def remove_item(self, order_id: int) -> None:
        pass

    @overrides
    def get_all_order_items(self, order_id: int) -> list[ItemModel]:
        pass

