from dataclasses import dataclass


@dataclass
class ItemModel:
    product_id: int
    quantity: int
    id: int = None
    order_id: int = None
