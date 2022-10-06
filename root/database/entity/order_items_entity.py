from sqlalchemy import String, Column, Integer, ForeignKey, Float

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class OrderItemsEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'order_items'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    order_id: Column = Column(Integer, ForeignKey('orders.id'))
    product_id: Column = Column(Integer, ForeignKey('products.id'))
    quantity: Column = Column(Integer)

