from abc import ABCMeta, abstractmethod
from root.item.item_model import ItemModel


class AbstractOrder(metaclass=ABCMeta):

    @abstractmethod
    def get_order_id(self) -> str | int:
        pass

    @abstractmethod
    def set_order_id(self, order_id: str | int) -> None:
        pass

    @abstractmethod
    def get_total_cost(self) -> float:
        pass

    @abstractmethod
    def set_total_cost(self, total_cost: float) -> None:
        pass

    @abstractmethod
    def get_all_order_items(self) -> None | list[ItemModel]:
        pass
