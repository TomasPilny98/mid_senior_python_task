from root.customer.customer_model import CustomerModel
from root.customer.customer import Customer
from injector import singleton


@singleton
class CustomerManager:

    def create_customer(self, customer_model: CustomerModel) -> None:
        # todo persist in db
        pass

    def delete_customer_by_phone(self, phone_number: int) -> None:
        # todo delete from db
        pass
