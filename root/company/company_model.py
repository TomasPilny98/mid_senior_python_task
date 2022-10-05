from root.customer.customer_contact_model import CustomerContactModel
from dataclasses import dataclass


@dataclass
class CompanyModel:
    contacts: CustomerContactModel
    dic: int
    ico: int
