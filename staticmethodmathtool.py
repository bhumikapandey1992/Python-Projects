# Static method - General utility method
#               - Belongs to the class,
#               - But it doesn't need access to the instance (self),
#               - And it doesn’t need access to the class (cls) either.
#               - define it using the @staticmethod decorator
# Example 1: Utility Method
# Example 2: Validation Helper
# Example 3: With Class and Static Methods Together


# Example 1: Utility Method

class MathTools:

    def __init__(self, number):
        self.number = number

    def check_even(self):
        if MathTools.is_even(self.number):
            print(f"{self.number} is even.")
        else:
            print(f"{self.number} is odd.")

    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
print(MathTools.is_even(4))

m1 = MathTools(10)
m2 = MathTools(7)

m1.check_even()
m2.check_even()