from enum import Enum

"""Enumerations"""


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def get_day(number: int):
    print(Weekday(number).name)
    # print(Weekday(number).value)


get_day(1)
get_day(2)
get_day(3)


"""Exercise"""


class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELED = 4


class Order:

    status = OrderStatus.PENDING

    def __init__(self, order_id) -> None:
        """Initialize an order with an ID and status."""
        self.order_id = order_id

    def ship(self):
        if self.status == OrderStatus.PENDING:
            self.status = OrderStatus.SHIPPED
            self.display_status()
        else:
            print("The order has already been shipped or canceled.")

    def deliver(self):
        if self.status == OrderStatus.SHIPPED:
            self.status = OrderStatus.DELIVERED
            self.display_status()
        else:
            print("The order needs to be shipped before it can be delivered.")

    def cancel(self):
        if self.status != OrderStatus.DELIVERED:
            self.status = OrderStatus.CANCELED
            self.display_status()
        else:
            print("The order has already been delivered and cannot be canceled.")

    def display_status(self):
        """Display the current status of the order."""
        print(f"Order ID: {self.order_id}, Status: {self.status.name}")


order_1 = Order(101)
order_1.display_status()
order_1.ship()
order_1.deliver()
order_1.cancel()
