from typing import Optional
from injector import singleton, inject
from overrides import overrides

from root.model.customer_model import CustomerModel
from root.database.abstract.abstract_customers_repository import AbstractCustomersRepository
from root.database.repository.customers_repository import CustomersRepository


@singleton
class CustomerManager(AbstractCustomersRepository):

    @inject
    def __init__(self, customers_repository: CustomersRepository):
        self._customers_repository: CustomersRepository = customers_repository

    @overrides
    def add_customer(self, customer_model: CustomerModel) -> None:
        self._customers_repository.add_customer(customer_model)

    @overrides
    def delete_customer(self, customer_id: int) -> None:
        self._customers_repository.delete_customer(customer_id)

    @overrides
    def get_all_customers_data(self) -> Optional[list[CustomerModel]]:
        return self._customers_repository.get_all_customers_data()


