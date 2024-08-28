from item import Item 
from phone import Phone

item1 = Item("MyItem", 750)
item1.name = "OtherItem"
 
print(item1.name)

# Item.instantiate_from_csv()
# print(Item.all)

# item1 = Item("ABCPhone", 500, 5)
# phone2 = Phone("ABSPhone", 700, 5, 1)

# print(phone2.calculate_total_price())
# print(Item.all)
    
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
