from sqlalchemy import Column, Integer, ForeignKey

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class OrderItemsEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'order_items'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    order_id: Column = Column(Integer, ForeignKey('orders.id'))
    product_id: Column = Column(Integer, ForeignKey('products.id'))
    quantity: Column = Column(Integer)


injector.get(RepositoryManager).base.metadata.create_all(injector.get(RepositoryManager).engine)
injector.get(RepositoryManager).session_scope.commit()
injector.get(RepositoryManager).session.remove()
