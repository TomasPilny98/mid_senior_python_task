from abc import ABCMeta, abstractmethod


class AbstractCustomer(metaclass=ABCMeta):

    @abstractmethod
    def set_email(self, email_address: str) -> None:
        pass

    @abstractmethod
    def get_email(self) -> str:
        pass

    @abstractmethod
    def set_phone(self, phone_number: int) -> None:
        pass

    @abstractmethod
    def get_phone(self) -> int:
        pass
