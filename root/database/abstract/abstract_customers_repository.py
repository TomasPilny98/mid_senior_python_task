from abc import ABCMeta, abstractmethod
from typing import Optional

from root.database.entity.customers_entity import CustomersEntity
from root.customer.customer_model import CustomerModel


class AbstractCustomersRepository(metaclass=ABCMeta):

    @abstractmethod
    def add_customer(self, person_customer_entity: CustomersEntity) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_all_customers_data(self) -> Optional[list[CustomerModel]]:
        pass

