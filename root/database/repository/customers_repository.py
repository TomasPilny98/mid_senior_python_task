from typing import Optional
from overrides import overrides
from injector import inject, singleton

from root.customer.customer_model import CustomerModel
from root.database.abstract.abstract_customers_repository import AbstractCustomersRepository
from root.database.entity.customers_entity import CustomersEntity
from root.database.manager.thread_session_request_manager import ThreadSessionRequestManager
from root.rest.json_convertor import JsonConvertor


@singleton
class CustomersRepository(AbstractCustomersRepository):

    @inject
    def __init__(self, db_session: ThreadSessionRequestManager, json_convertor: JsonConvertor):
        self._db_session: ThreadSessionRequestManager = db_session
        self._json_convertor: JsonConvertor = json_convertor

    @overrides
    def add_customer(self, person_customer_entity: CustomersEntity) -> None:
        pass

    @overrides
    def delete_customer(self, customer_id: int) -> None:
        pass

    @overrides
    def get_all_customers_data(self) -> Optional[list[CustomerModel]]:
        pass




