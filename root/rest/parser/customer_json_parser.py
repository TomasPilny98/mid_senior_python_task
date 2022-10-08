from root.model.customer_model import CustomerModel
from root.model.customer_contact_model import CustomerContactModel
from root.model.company_model import CompanyModel
from root.model.person_model import PersonModel
from root.enum.json_data_enum import JsonDataEnum
from injector import singleton
from datetime import datetime, date


@singleton
class CustomerJsonParser:

    # TODO client uses CUSTOMER_TYPE and db uses IS_PERSON which causes conflict, unite to one or another
    # TODO dont send two different jsons for person and company but unite it as well

    def to_customer_model(self, raw_json: dict, customer_id: int = None) -> CustomerModel:
        customer_type: PersonModel | CompanyModel

        if raw_json[str(JsonDataEnum.IS_PERSON)]:
            customer_type = self.to_person_model(raw_json)
        elif not raw_json[str(JsonDataEnum.IS_PERSON)]:
            customer_type = self.to_company_model(raw_json)
        else:
            raise Exception('Unknown customer type, JSON parse error')

        return CustomerModel(customer_data=customer_type, id=customer_id)

    def to_person_model(self, raw_json: dict) -> PersonModel:
        return PersonModel(first_name=raw_json[str(JsonDataEnum.FIRST_NAME)],
                           last_name=raw_json[str(JsonDataEnum.LAST_NAME)],
                           birth_date=self.get_birth_date_in_datetime(raw_json[str(JsonDataEnum.BIRTH_DATE)]),
                           contacts=self.to_contacts_model(raw_json))

    def to_company_model(self, raw_json: dict) -> CompanyModel:
        return CompanyModel(contacts=self.to_contacts_model(raw_json),
                            dic=raw_json[str(JsonDataEnum.DIC)],
                            ico=raw_json[str(JsonDataEnum.ICO)])

    def get_birth_date_in_datetime(self, birth_date: date | str) -> date | str:
        if type(birth_date) is str:
            return self.convert_str_time_to_datetime(birth_date)
        else:
            return birth_date.isoformat()

    @staticmethod
    def convert_str_time_to_datetime(json_time: str) -> datetime.date:
        return datetime.strptime(json_time, '%d/%m/%Y').date()

    @staticmethod
    def to_contacts_model(raw_json: dict) -> CustomerContactModel:
        return CustomerContactModel(phone_number=raw_json[str(JsonDataEnum.PHONE_NUMBER)],
                                    email_address=raw_json[str(JsonDataEnum.EMAIL_ADDRESS)])
