from abc import ABCMeta, abstractmethod

from root.order.order_model import OrderModel
from root.item.item_model import ItemModel


class AbstractOrdersRepository(metaclass=ABCMeta):

    @abstractmethod
    def add_order(self, customer_id: int, order_model: OrderModel) -> None:
        pass

    @abstractmethod
    def remove_order(self, order_id: int) -> None:
        pass

    @abstractmethod
    def add_item(self, order_id: int, item_model: ItemModel) -> None:
        pass

    @abstractmethod
    def remove_item(self, order_id: int) -> None:
        pass

    @abstractmethod
    def get_all_order_items(self, order_id: int) -> list[ItemModel]:
        pass
