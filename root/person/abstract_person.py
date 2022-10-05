from abc import ABCMeta, abstractmethod
from datetime import datetime


class AbstractPerson(metaclass=ABCMeta):

    @abstractmethod
    def set_first_name(self, first_name: str) -> None:
        pass

    @abstractmethod
    def set_last_name(self, last_name: str) -> None:
        pass

    @abstractmethod
    def set_birth_date(self, date: datetime) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_birth_date(self) -> datetime:
        pass
