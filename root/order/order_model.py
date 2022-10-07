from dataclasses import dataclass

from root.item.item_model import ItemModel


@dataclass
class OrderModel:
    customer_id: int
    items: list[ItemModel]
    internal_id: int | None = None
    total_cost: float | None = None

