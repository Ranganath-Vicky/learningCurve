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
        self.name = name #Dynamic attribute for class instance
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

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
        return f"Item('{self.name}',{self.price}, {self.quantity})"

class Phone(Item):     ## Child classes
    all = []
    def __init__(self, name: str, price: float, quantity=1, broken_phones = 0):
        
        #call to super function to have access to all attributes and methods from parent class
        super().__init__(
            name, price, quantity
        )
        # Run validation to recieve arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than 0!"
        
        # Assign to self object - instance attribute
        self.broken_phones = broken_phones

        # Actions to execute
        Phone.all.append(self)


phone1 = Phone("ABCPhone", 500, 5, 1)
phone2 = Phone("ABSPhone", 700, 5, 1)

print(phone1.calculate_total_price())
    
# Item.is_integer(7.0) # calling a static method
# Item.instantiate_from_csv() # Calling class method 

# print(Item.pay_rate) # accesing class attributes from class levels
# print(item1.pay_rate) # accessing class attribute from instance level

# print(Item.__dict__) # attributes at class level 
# print(item1.__dict__) # attributes at instance level

# item1 = Item("Phone", 100, 5) # creating an instance of a class
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop", 1000, 2)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.all)
# for each in Item.all:
#     print(each.name)
