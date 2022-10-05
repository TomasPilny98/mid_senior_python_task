from abc import ABCMeta, abstractmethod


class AbstractItem(metaclass=ABCMeta):

    @abstractmethod
    def get_item_id(self) -> int:
        pass

    @abstractmethod
    def set_item_id(self, item_id: int) -> None:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def set_price(self, price: float) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def set_description(self, description: str) -> None:
        pass
