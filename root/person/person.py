from datetime import datetime
from overrides import overrides

from root.person.abstract_person import AbstractPerson
from root.customer.abstract_customer import AbstractCustomer
from root.person.person_model import PersonModel
from root.customer.customer_contact_model import CustomerContactModel


class Person(AbstractCustomer, AbstractPerson):

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 birth_date: datetime,
                 contacts: CustomerContactModel):
        self._person_model: PersonModel = PersonModel(first_name, last_name, birth_date, contacts)

    @overrides
    def set_email(self, email_address: str) -> None:
        self._person_model.contacts.email_address = email_address

    @overrides
    def get_email(self) -> str:
        return self._person_model.contacts.email_address

    @overrides
    def set_phone(self, phone_number: int) -> None:
        self._person_model.contacts.phone_number = phone_number

    @overrides
    def get_phone(self) -> int:
        return self._person_model.contacts.phone_number

    @overrides
    def set_first_name(self, first_name: str) -> None:
        self._person_model.first_name = first_name

    @overrides
    def set_last_name(self, last_name: str) -> None:
        self._person_model.last_name = last_name

    @overrides
    def set_birth_date(self, date: datetime) -> None:
        self._person_model.birth_date = date

    @overrides
    def get_name(self) -> str:
        return self._person_model.first_name + ' ' + self._person_model.last_name

    @overrides
    def get_birth_date(self) -> datetime:
        return self._person_model.birth_date
