from root.model.item_model import ItemModel
from root.model.order_model import OrderModel
from root.enum.json_data_enum import JsonDataEnum
from injector import singleton


@singleton
class OrderJsonParser:

    def to_order_model(self, raw_json: dict) -> OrderModel:
        items: list[ItemModel] = []
        for product_id in raw_json[str(JsonDataEnum.PRODUCTS)]:
            items.append(self._to_item_model(product_id))

        return OrderModel(customer_id=raw_json[str(JsonDataEnum.CUSTOMER_ID)],
                          items=items)

    @staticmethod
    def _to_item_model(raw_json: dict) -> ItemModel:
        return ItemModel(product_id=raw_json[str(JsonDataEnum.PRODUCT_ID)],
                         quantity=raw_json[str(JsonDataEnum.QUANTITY)])
