import csv


class Item: 
    #class attribute 
    pay_rate = 0.8 # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=1): #default values and validating the datatypes for input arguments
        
        # Run validation to recieve arguments
        assert price >= 0, f"Price {price} is not greater than 50!" 
        assert quantity >= 0, f"Quantity {quantity} is not greater than 0!"
        
        # Assign to self object - instance attribute
        self._name = name #Dynamic attribute for class instance
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property decorator - read only attribute 
    def name(self):
        return self._name

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod # Decorator to convert a method to classmethod
    def instantiate_from_csv(cls): # Class Method - class reference is passed as input argument
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name = item.get('name'), 
                 price = float(item.get('price')),
                 quantity= int(item.get('quantity')),
                 )
    
    # Static method
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price}, {self.quantity})"
