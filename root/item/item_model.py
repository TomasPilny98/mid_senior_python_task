from dataclasses import dataclass


@dataclass
class ItemModel:
    item_id: int
    price: float
    description: str
