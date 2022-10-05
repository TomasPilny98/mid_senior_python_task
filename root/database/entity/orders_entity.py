from sqlalchemy import String, Column, Integer, ForeignKey, Float

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class OrdersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'orders'

    order_id: Column = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    order_number: Column = Column(Integer)
    person_customer_email: Column = Column(String(100), ForeignKey('person_customers.email'))
    company_customer_email: Column = Column(String(100), ForeignKey('company_customers.email'))
    total_price: Column = Column(Float)
