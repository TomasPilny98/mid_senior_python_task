from dataclasses import dataclass


@dataclass
class ItemModel:
    item_id: int
    item_name: str
    price: float
    description: str
