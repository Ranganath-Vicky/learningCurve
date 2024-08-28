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
        self.__name = name #Dynamic attribute for class instance
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property decorator - read only attribute 
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        return self.__price

    def apply_increment(self, value):
        self.__price = self.__price + self.__price * value
        return self.__price
    
    @name.setter # for setting a value to a attribute 
    def name(self, value):
        if len(value) > 10:
            raise Exception("Name length is long")
        else:
            self.__name = value
            return self.__name 

    def calculate_total_price(self):
        return self.__price * self.quantity
    
    

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

    def __connect(self):
        pass

    def __prepare_body(self):
        return f"""
        Hello SomeOne. 
        We have {self.name} {self.quantity} times.
        Thank you"""
    
    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()
