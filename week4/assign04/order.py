from product import Product


class Order():
    """ class order has  an id and  
    an array of products that are from Product class
    with function to calculate  subtotal, tax, total and display information 
    """

    def __init__(self) -> None:
        self.id = ""
        self.products = []

    def get_subtotal(self):
        sum = 0
        for product in self.products:
            sum += product.price * product.quantity
        return sum

    def get_tax(self):
        return self.get_subtotal() * 0.065
        

    def get_total(self):
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product: Product):
        self.products.append(product)

    def display_receipt(self):
        print(f'Order: {self.id}')
        for product in self.products:
            # I am using the method of the class product instead to write again the code
            product.display()
        print(f'Subtotal: ${self.get_subtotal():.2f}')
        print(f'Tax: ${self.get_tax():.2f}')
        print(f'Total: ${self.get_total():.2f}')
