from sqlalchemy import String, Column, Integer, DateTime, Boolean

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class CustomersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'customers'

    id: Column = Column(Integer, autoincrement=True, primary_key=True)
    first_name: Column = Column(String(50))
    last_name: Column = Column(String(50))
    birth_date: Column = Column(DateTime)
    ico: Column = Column(Integer)
    dic: Column = Column(Integer)
    phone_number: Column = Column(Integer, unique=True)
    email_address: Column = Column(String(100))
    is_person: Column = Column(Boolean)
