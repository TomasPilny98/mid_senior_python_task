from sqlalchemy import Column, Integer, ForeignKey, Float

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager
from root.database.entity.customers_entity import CustomersEntity


class OrdersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'orders'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    customer_id: Column = Column(Integer, ForeignKey(CustomersEntity.id))
    order_number: Column = Column(Integer)
    total_price: Column = Column(Float)


injector.get(RepositoryManager).base.metadata.create_all(injector.get(RepositoryManager).engine)
injector.get(RepositoryManager).session_scope.commit()
injector.get(RepositoryManager).session.remove()
