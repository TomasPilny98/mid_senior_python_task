from root.customer.customer_model import CustomerModel
from root.customer.customer_contact_model import CustomerContactModel
from root.company.company_model import CompanyModel
from root.order.order_model import OrderModel
from root.person.person_model import PersonModel
from root.item.item_model import ItemModel
from root.enum.json_data_enum import JsonDataEnum
from injector import singleton


@singleton
class JsonConvertor:

    def to_customer_model(self, raw_json: dict) -> CustomerModel:
        customer_type: PersonModel | CompanyModel

        if raw_json[str(JsonDataEnum.CUSTOMER_TYPE)] is None:
            raise Exception('JSON structure raised an error during parsing <CUSTOMER_TYPE>')
        elif raw_json[str(JsonDataEnum.CUSTOMER_TYPE)] == str(JsonDataEnum.PERSON):
            customer_type = self.to_person_model(raw_json)
        elif raw_json[str(JsonDataEnum.CUSTOMER_TYPE)] == str(JsonDataEnum.COMPANY):
            customer_type = self.to_company_model(raw_json)
        else:
            raise Exception('Unknown customer type, JSON parse error')

        return CustomerModel(customer_data=customer_type)

    def to_person_model(self, raw_json: dict) -> PersonModel:
        return PersonModel(first_name=raw_json[str(JsonDataEnum.FIRST_NAME)],
                           last_name=raw_json[str(JsonDataEnum.LAST_NAME)],
                           birth_date=raw_json[str(JsonDataEnum.BIRTH_DATE)],
                           contacts=self.to_contacts_model(raw_json))

    def to_company_model(self, raw_json: dict) -> CompanyModel:
        return CompanyModel(contacts=self.to_contacts_model(raw_json),
                            dic=raw_json[str(JsonDataEnum.DIC)],
                            ico=raw_json[str(JsonDataEnum.ICO)])

    @staticmethod
    def to_order_model(raw_json: dict) -> OrderModel:
        items: list[ItemModel] = []
        for item in raw_json[str(JsonDataEnum.ITEMS)]:
            items.append(ItemModel(item[str(JsonDataEnum.ITEM_ID)],
                                   item[str(JsonDataEnum.ITEM_NAME)],
                                   item[str(JsonDataEnum.PRICE)],
                                   item[str(JsonDataEnum.DESCRIPTION)]))
        return OrderModel(customer_id=raw_json[str(JsonDataEnum.CUSTOMER_ID)], items=items)

    @staticmethod
    def to_contacts_model(raw_json: dict) -> CustomerContactModel:
        return CustomerContactModel(phone_number=raw_json[str(JsonDataEnum.PHONE_NUMBER)],
                                    email_address=raw_json[str(JsonDataEnum.EMAIL_ADDRESS)])
