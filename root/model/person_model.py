from root.model.customer_contact_model import CustomerContactModel
from dataclasses import dataclass
from datetime import datetime


@dataclass
class PersonModel:
    first_name: str
    last_name: str
    birth_date: datetime.date
    contacts: CustomerContactModel
