from dataclasses import dataclass

from root.model.item_model import ItemModel


@dataclass
class OrderModel:
    customer_id: int
    items: list[ItemModel]
    id: int | None = None
    total_cost: float | None = None
    order_number: int = None


