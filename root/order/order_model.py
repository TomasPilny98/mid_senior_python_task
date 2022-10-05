from dataclasses import dataclass

from root.customer.customer_contact_model import CustomerContactModel
from root.item.item_model import ItemModel


@dataclass
class OrderModel:
    contacts: CustomerContactModel
    items: list[ItemModel]
    internal_id: int | None = None
    total_cost: float | None = None

