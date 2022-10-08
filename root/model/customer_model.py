from dataclasses import dataclass
from root.model.person_model import PersonModel
from root.model.company_model import CompanyModel


@dataclass
class CustomerModel:
    customer_data: PersonModel | CompanyModel
    id: int = None
