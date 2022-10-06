from abc import ABCMeta, abstractmethod
from root.database.entity.customers_entity import CustomersEntity


class AbstractCustomersRepository(metaclass=ABCMeta):
    pass
    #@abstractmethod
    #def add_person_customer(self, person_customer_entity: ):