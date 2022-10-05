from abc import ABCMeta, abstractmethod


class AbstractCompany(metaclass=ABCMeta):

    @abstractmethod
    def set_ico(self, ico: int) -> None:
        pass

    @abstractmethod
    def get_ico(self) -> int:
        pass

    @abstractmethod
    def set_dic(self, dic: int) -> None:
        pass

    @abstractmethod
    def get_dic(self) -> int:
        pass
   