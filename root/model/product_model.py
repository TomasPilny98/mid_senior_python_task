from dataclasses import dataclass


@dataclass
class ProductModel:
    product_name: str
    price: float
    description: str
    id: int = None
