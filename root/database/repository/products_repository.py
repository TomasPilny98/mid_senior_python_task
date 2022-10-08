from injector import singleton, inject
from overrides import overrides

from root.database.abstract.abstract_products_repository import AbstractProductsRepository
from root.database.entity.convertor.entity_convertor import EntityConvertor
from root.database.manager.thread_session_request_manager import ThreadSessionRequestManager
from root.model.product_model import ProductModel


@singleton
class ProductsRepository(AbstractProductsRepository):

    @inject
    def __init__(self, db_session: ThreadSessionRequestManager, entity_convertor: EntityConvertor):
        self._db_session: ThreadSessionRequestManager = db_session
        self._entity_convertor: EntityConvertor = entity_convertor

    @overrides
    def create_product(self, product_model: ProductModel) -> None:
        try:
            entity = self._entity_convertor.product_model_to_entity(product_model)
            self._db_session.session.add(entity)
            self._db_session.safe_commit()
        except Exception as e:
            print('db error - create_product failed', e)

    @overrides
    def delete_product(self, product_id: int) -> None:
        pass

    @overrides
    def update_product(self, updated_product_model: ProductModel) -> None:
        pass
