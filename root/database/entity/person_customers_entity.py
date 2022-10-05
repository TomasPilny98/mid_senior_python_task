from sqlalchemy import String, Column, Integer, DateTime

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class PersonCustomersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'person_customers'

    customer_id: Column = Column(Integer, autoincrement=True, unique=True)
    first_name: Column = Column(String(50))
    last_name: Column = Column(String(50))
    birth_date: Column = Column(DateTime)
    phone: Column = Column(Integer, unique=True)
    email: Column = Column(String(100), unique=True, primary_key=True)
