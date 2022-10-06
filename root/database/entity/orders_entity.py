from sqlalchemy import String, Column, Integer, ForeignKey, Float

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class OrdersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'orders'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    customer_id: Column = Column(Integer, ForeignKey('customers.id'))
    order_number: Column = Column(Integer)
    total_price: Column = Column(Float)
