from sqlalchemy import Column, Integer, ForeignKey

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager
from root.database.entity.orders_entity import OrdersEntity
from root.database.entity.products_entity import ProductsEntity


class ItemsEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'order_items'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    order_id: Column = Column(Integer, ForeignKey(OrdersEntity.id))
    product_id: Column = Column(Integer, ForeignKey(ProductsEntity.id))
    quantity: Column = Column(Integer)


injector.get(RepositoryManager).base.metadata.create_all(injector.get(RepositoryManager).engine)
injector.get(RepositoryManager).session_scope.commit()
injector.get(RepositoryManager).session.remove()
