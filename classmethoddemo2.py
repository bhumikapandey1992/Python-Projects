
# NAMED CONSTRUCTORS

class Pizza:
    def __init__(self,size,toppings):
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls("medium",["cheese","tomato"])
    
    @classmethod
    def pepperoni(cls):
        return cls("large",["cheese", "pepperoni"])
    
p1 = Pizza.margherita()
p2 = Pizza.pepperoni()
print(f"Size: {p1.size} Toppings: {p1.toppings}")
print(f"Size: {p2.size} Toppings: {p2.toppings}")