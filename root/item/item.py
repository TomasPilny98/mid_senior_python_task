from root.item.item_model import ItemModel
from root.item.abstract_item import AbstractItem
from overrides import overrides


class Item(AbstractItem):

    def __init__(self, item_id: int, item_name: str, price: float, description: str):
        self._item_model: ItemModel = ItemModel(item_id, item_name, price, description)

    @overrides
    def get_item_id(self) -> int:
        return self._item_model.item_id

    @overrides
    def set_item_id(self, item_id: int) -> None:
        self._item_model.item_id = item_id

    @overrides
    def get_price(self) -> float:
        return self._item_model.price

    @overrides
    def set_price(self, price: float) -> None:
        self._item_model.price = price

    @overrides
    def get_description(self) -> str:
        return self._item_model.description

    @overrides
    def set_description(self, description: str) -> None:
        self._item_model.description = description
