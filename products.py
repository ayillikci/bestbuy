class Product:
    def __init__(self, name:str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0 :
            raise ValueError("Product can price can not be below 0")
        if quantity < 0 :
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        def get_quantity(self):
            if not type(self) == int:
                raise ValueError("Product quantity needs to be an integer number")
            return self.quantity

        def set_quantity(self, quantity:int):
            if quantity < 0 :
                raise ValueError("Product quantity can not be below 0")

            self.quantity = quantity

            if quantity == 0 :
                self.deactive()

        def activate(self):
            self.active = True

        def deactivate(self):
            self.active = False


