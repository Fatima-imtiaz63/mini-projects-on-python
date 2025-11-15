"""class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
   
   def to_fehrenheit(self, fehrenheit):
   return (self.celsius *9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15
    
c = float(input("Enter temperature in celcius:"))
temp = Temperature(c)
print("fehrenheit:", temp.to_fehrenheit)
print("kelvin :", temp.to_kelvin)"""

# SIMPLE E-COMMERCE CART SYSTEM
class products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class cartItem:
    def __init__(self,product, quantity):
        self.product = product
        self.quantity = quantity

def item_total(self):
        return self.product.price* self.quantity

p1 = products("shirt", 800)
p2 = products ("Shoes", 2000)
p3 = products("Bags", 1500)

c1 =cartItem(p1, 2)
c2 = cartItem(p2,1)
c3 =cartItem(p3, 3)

total = c1.Item_total() + c2.Item_total() +c3.Item_total()
print("Total bill", total)
        