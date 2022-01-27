from order import Order


class Customer():
    """
    customer class has two function to display 
    display all the receipts has to iterate  the array of oorders
    """

    def __init__(self) -> None:
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        return len(self.orders)

    def get_total(self):
        total = 0
        for order in self.orders:
            total += order.get_total()
        return total

    def add_order(self, order: Order):
        self.orders.append(order)

    def display_summary(self):
        print(f"Summary for customer '{self.id}':")
        print(f"Name: {self.name}")
        print(f'Orders: {self.get_order_count()}')
        print(f'Total: ${self.get_total():.2f}')

    def display_receipts(self):
        print(f"Detailed receipts for customer '{self.id}':")
        print(f"Name: {self.name}")
        for order in self.orders:
            #  this print  need to be before to  pass the test
            print()
            order.display_receipt()
