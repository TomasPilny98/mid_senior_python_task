from injector import singleton, inject

from root.database.entity.customers_entity import CustomersEntity
from root.database.entity.items_entity import ItemsEntity
from root.database.entity.orders_entity import OrdersEntity
from root.database.entity.products_entity import ProductsEntity
from root.enum.json_data_enum import JsonDataEnum
from root.model.customer_model import CustomerModel
from root.model.item_model import ItemModel
from root.model.order_model import OrderModel
from root.model.person_model import PersonModel
from root.model.product_model import ProductModel
from root.rest.parser.customer_json_parser import CustomerJsonParser


@singleton
class EntityConvertor:

    @inject
    def __init__(self, json_convertor: CustomerJsonParser):
        self._json_convertor: CustomerJsonParser = json_convertor

    # MODEL TO ENTITY

    @staticmethod
    def customer_model_to_entity(customer_model: CustomerModel) -> CustomersEntity:

        if type(customer_model.customer_data) is PersonModel:
            is_person = True
            ico = None
            dic = None
            first_name = customer_model.customer_data.first_name
            last_name = customer_model.customer_data.last_name
            birth_date = customer_model.customer_data.birth_date
        else:
            is_person = False
            ico = customer_model.customer_data.ico
            dic = customer_model.customer_data.dic
            first_name = None
            last_name = None
            birth_date = None

        return CustomersEntity(id=customer_model.id,
                               first_name=first_name,
                               last_name=last_name,
                               birth_date=birth_date,
                               ico=ico,
                               dic=dic,
                               phone_number=customer_model.customer_data.contacts.phone_number,
                               email_address=customer_model.customer_data.contacts.email_address,
                               is_person=is_person)

    @staticmethod
    def order_model_to_entity(order_model: OrderModel) -> OrdersEntity:
        return OrdersEntity(id=order_model.id,
                            customer_id=order_model.customer_id,
                            order_number=order_model.order_number,
                            total_price=order_model.total_cost)

    @staticmethod
    def item_model_to_entity(item_model: ItemModel) -> ItemsEntity:
        return ItemsEntity(id=item_model.id,
                           order_id=item_model.order_id,
                           product_id=item_model.product_id,
                           quantity=item_model.quantity)

    @staticmethod
    def product_model_to_entity(product_model: ProductModel) -> ProductsEntity:
        return ProductsEntity(id=product_model.id,
                              product_name=product_model.product_name,
                              price=product_model.price,
                              description=product_model.description)

    # DB RAW TO MODEL

    def customer_db_raw_to_model(self, db_raws_data: list[dict]) -> list[CustomerModel]:
        if len(db_raws_data) > 0:
            customer_models: list[CustomerModel] = []
            for db_raw in db_raws_data:
                result = vars(db_raw)
                result.pop('_sa_instance_state')
                _id: int = result[str(JsonDataEnum.ID)]
                customer_models.append(self._json_convertor.to_customer_model(result.copy(), _id))
            return customer_models

    def order_db_raw_to_model(self, db_raws_data: list[dict]) -> list[OrderModel]:
        if len(db_raws_data) > 0:
            order_models: list[OrderModel] = []
            for db_raw in db_raws_data:
                result = vars(db_raw)
                result.pop('_sa_instance_state')
                order_models.append(self._json_convertor.to_order_model(result.copy()))
            return order_models

    def item_db_raw_to_model(self, db_raws_data: list[dict]) -> ItemModel:
        pass

    def product_db_raw_to_model(self, db_raws_data: list[dict]) -> ProductModel:
        pass
