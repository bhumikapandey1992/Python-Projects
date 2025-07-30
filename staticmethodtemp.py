# Example 3: With Class and Static Methods Together


class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    @classmethod
    def from_fahrenheit(cls,f):
        c = (f - 32) * 5/9
        return cls(c)
    
    @staticmethod
    def is_freezing(celsius):
        return celsius <=0
    
temp = Temperature(0)
print(temp.to_fahrenheit())
print(Temperature.is_freezing(0))
temp2 = Temperature.from_fahrenheit(50)
print(temp2.celsius)