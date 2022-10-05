from abc import ABCMeta, abstractmethod
from root.database.entity.person_customers_entity import PersonCustomersEntity
from root.database.entity.company_customers_entity import CompanyCustomersEntity


class AbstractCustomersRepository(metaclass=ABCMeta):
    pass
    #@abstractmethod
    #def add_person_customer(self, person_customer_entity: ):