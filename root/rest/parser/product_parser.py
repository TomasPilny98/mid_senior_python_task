from injector import singleton

from root.enum.json_data_enum import JsonDataEnum
from root.model.product_model import ProductModel


@singleton
class ProductParser:

    @staticmethod
    def to_product_model(raw_json: dict) -> ProductModel:
        return ProductModel(product_name=raw_json[str(JsonDataEnum.PRODUCT_NAME)],
                            price=raw_json[str(JsonDataEnum.PRICE)],
                            description=raw_json[str(JsonDataEnum.DESCRIPTION)])
