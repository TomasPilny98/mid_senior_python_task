from abc import ABCMeta, abstractmethod

from root.model.product_model import ProductModel


class AbstractProductsRepository(metaclass=ABCMeta):

    @abstractmethod
    def create_product(self, product_model: ProductModel) -> None:
        pass

    @abstractmethod
    def delete_product(self, product_id: int) -> None:
        pass

    @abstractmethod
    def update_product(self, updated_product_model: ProductModel) -> None:
        pass
