from sqlalchemy import String, Column, Integer, Float

from root.main.dependency_injection_init import injector
from root.database.manager.repository_manager import RepositoryManager


class ProductsEntity(injector.get(RepositoryManager).base):
    __tablename__ = 'products'

    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    product_name: Column = Column(String(255))
    description: Column = Column(String(255))
    unit_price: Column = Column(Float)

