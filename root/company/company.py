from root.company.abstract_company import AbstractCompany
from root.customer.abstract_customer import AbstractCustomer
from root.company.company_model import CompanyModel
from root.customer.customer_contact_model import CustomerContactModel

from overrides import overrides


class Company(AbstractCompany, AbstractCustomer):

    def __init__(self, ico: int, dic: int, contacts: CustomerContactModel):
        self._company_model: CompanyModel = CompanyModel(contacts, dic, ico)

    @overrides
    def set_ico(self, ico: int) -> None:
        self._company_model.ico = ico

    @overrides
    def get_ico(self) -> int:
        return self._company_model.ico

    @overrides
    def set_dic(self, dic: int) -> None:
        self._company_model.dic = dic

    @overrides
    def get_dic(self) -> int:
        return self._company_model.dic

    @overrides
    def set_email(self, email_address: str) -> None:
        self._company_model.contacts.email_address = email_address

    @overrides
    def get_email(self) -> str:
        return self._company_model.contacts.email_address

    @overrides
    def set_phone(self, phone_number: int) -> None:
        self._company_model.contacts.phone_number = phone_number

    @overrides
    def get_phone(self) -> int:
        return self._company_model.contacts.phone_number
