class Product():
    """  the class create a product with 
    two methods to get  the total price and display information
    """

    def __init__(self, id: str, name: str, price: float, quantity: int) -> None:
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        # to convert the number with 2 decimals
        return self.price * self.quantity

    def display(self):
        print(f'{self.name} ({self.quantity}) - ${self.get_total_price():.2f}')
