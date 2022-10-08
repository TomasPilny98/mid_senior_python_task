from abc import ABCMeta, abstractmethod
from typing import Optional

from root.model.customer_model import CustomerModel


class AbstractCustomersRepository(metaclass=ABCMeta):

    @abstractmethod
    def add_customer(self, customer_model: CustomerModel) -> None:
        pass

    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        pass

    @abstractmethod
    def get_all_customers_data(self) -> Optional[list[CustomerModel]]:
        pass

