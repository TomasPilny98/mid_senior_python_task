from root.order.order_model import OrderModel
from root.item.item_model import ItemModel
from root.order.abstract_order import AbstractOrder
from overrides import overrides


class Order(AbstractOrder):

    def __init__(self,
                 customer_id: int,
                 items: list[ItemModel],
                 internal_id: int,
                 total_cost: float):
        self._order_model: OrderModel = OrderModel(customer_id, items, internal_id, total_cost)

    @overrides
    def get_order_id(self) -> str | int:
        return self._order_model.internal_id

    @overrides
    def set_order_id(self, order_id: str | int) -> None:
        self._order_model.internal_id = order_id

    @overrides
    def get_total_cost(self) -> float:
        return self._order_model.total_cost

    @overrides
    def set_total_cost(self, total_cost: float) -> None:
        self._order_model.total_cost = total_cost

    @overrides
    def get_all_order_items(self) -> None | list[ItemModel]:
        return self._order_model.items
