from injector import singleton
from root.order.order import Order, OrderModel


@singleton
class OrderManager:

    def create_order(self, order_model: OrderModel) -> Order:
        pass

    def update_order(self, order_id: int) -> None:
        pass

    def delete_order(self, order_id: int) -> None:
        pass
