from datetime import datetime
import json


class Order:
    def __init__(self, order_id, customer, items, discount=0):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of (name, price, qty)
        self.created_at = datetime.now()

    def total_price(self):
        return sum(price * qty for _, price, qty in self.items)

    def summary(self):
        return {
            "id": self.order_id,
            "customer": self.customer,
            "total_price": self.total_price(),
            "created_at": self.created_at.isoformat(),
        }


class OrderManager:
    def __init__(self, storage_file="orders.json"):
        self.orders = {}
        self.storage_file = storage_file

    def create_order(self, order_id, customer, items, discount=0):
        order = Order(order_id, customer, items, discount)
        self.orders[order_id] = order
        self.save_to_disk()
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def get_total_revenue(self):
        return sum(order.total_price() for order in self.orders.values())

    def save_to_disk(self):
        data = {oid: order.summary() for oid, order in self.orders.items()}
        with open(self.storage_file, "w") as f:
            json.dump(data, f, indent=2)


if __name__ == "__main__":
    manager = OrderManager()

    manager.create_order(1, "Alice", [("Keyboard", 50, 1), ("Mouse", 25, 2)])

    print(manager.get_total_revenue())
