from item import Item

class Phone(Item):     ## Child classes
    def __init__(self, name: str, price: float, quantity=1, broken_phones = 0):
        
        #call to super function to have access to all attributes and methods from parent class
        super().__init__(
            name, price, quantity
        )
        # Run validation to recieve arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than 0!"
        
        # Assign to self object - instance attribute
        self.broken_phones = broken_phones
