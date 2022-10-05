from sqlalchemy import String, Column, Integer

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class CompanyCustomersEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'company_customers'

    customer_id: Column = Column(Integer, autoincrement=True, unique=True)
    ico: Column = Column(Integer)
    dic: Column = Column(Integer)
    phone: Column = Column(Integer, unique=True)
    email: Column = Column(String(100), unique=True, primary_key=True)


