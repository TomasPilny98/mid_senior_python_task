from typing import Optional
from overrides import overrides
from injector import inject, singleton

from root.database.entity.convertor.entity_convertor import EntityConvertor
from root.model.customer_model import CustomerModel
from root.database.abstract.abstract_customers_repository import AbstractCustomersRepository
from root.database.entity.customers_entity import CustomersEntity
from root.database.manager.thread_session_request_manager import ThreadSessionRequestManager
from root.rest.parser.customer_json_parser import CustomerJsonParser


@singleton
class CustomersRepository(AbstractCustomersRepository):

    @inject
    def __init__(self,
                 db_session: ThreadSessionRequestManager,
                 json_convertor: CustomerJsonParser,
                 entity_convertor: EntityConvertor):
        self._db_session: ThreadSessionRequestManager = db_session
        self._json_convertor: CustomerJsonParser = json_convertor
        self._entity_convertor: EntityConvertor = entity_convertor

    @overrides
    def add_customer(self, customer_model: CustomerModel) -> None:
        try:
            entity = self._entity_convertor.customer_model_to_entity(customer_model)
            self._db_session.session.add(entity)
            self._db_session.safe_commit()
        except Exception as e:
            print('db error - add_customer failed', e)

    @overrides
    def delete_customer(self, customer_id: int) -> None:
        try:
            self._db_session.session.query(CustomersEntity).filter(CustomersEntity.id == customer_id).delete()
            self._db_session.safe_commit()
        except Exception as e:
            print('db error - delete_customer failed', e)

    @overrides
    def get_all_customers_data(self) -> Optional[list[CustomerModel]]:
        try:
            customers_raws: list[dict] = self._db_session.session.query(CustomersEntity).all()
            return self._entity_convertor.customer_db_raw_to_model(customers_raws)
        except Exception as e:
            print('db error - get_all_customers failed', e)
