from enum import Enum


class JsonDataEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

    FIRST_NAME = 'firstName'
    LAST_NAME = 'lastName'
    BIRTH_DATE = 'birthDate'

    ICO = 'ico'
    DIC = 'dic'

    CONTACTS = 'contacts'
    PHONE_NUMBER = 'phoneNumber'
    EMAIL_ADDRESS = 'emailAddress'

    ORDER_ID = 'orderId'
    TOTAL_COST = 'totalCost'

    ITEMS = 'items'
    ITEM_ID = 'itemId'
    PRICE = 'price'
    DESCRIPTION = 'description'

    CUSTOMER_TYPE = 'customerType'
    PERSON = 'person'
    COMPANY = 'company'
