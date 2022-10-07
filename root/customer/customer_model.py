from dataclasses import dataclass
from root.person.person_model import PersonModel
from root.company.company_model import CompanyModel
from root.order.order_model import OrderModel


@dataclass
class CustomerModel:
    customer_data: PersonModel | CompanyModel
    orders: list[OrderModel] | None = None
