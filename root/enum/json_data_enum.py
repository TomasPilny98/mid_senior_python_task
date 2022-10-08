from enum import Enum


class JsonDataEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)

    ID = 'id'

    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'
    BIRTH_DATE = 'birth_date'

    ICO = 'ico'
    DIC = 'dic'

    CONTACTS = 'contacts'
    PHONE_NUMBER = 'phone_number'
    EMAIL_ADDRESS = 'email_address'

    ORDER_ID = 'order_id'
    TOTAL_COST = 'total_cost'

    QUANTITY = 'quantity'
    PRODUCTS = 'products'
    PRODUCT_ID = 'product_id'
    PRODUCT_NAME = 'product_name'
    PRICE = 'price'
    DESCRIPTION = 'description'

    IS_PERSON = 'is_person'
    CUSTOMER_ID = 'customer_id'
    PERSON = 'person'
    COMPANY = 'company'
