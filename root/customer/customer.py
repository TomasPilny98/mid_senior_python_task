from root.customer.customer_model import CustomerModel
from root.person.person_model import PersonModel
from root.company.company_model import CompanyModel
from root.order.order_model import OrderModel


class Customer:

    def __init__(self, customer_type: PersonModel | CompanyModel, order: list[OrderModel]):
        self._customer_model: CustomerModel = CustomerModel(customer_type, order)
