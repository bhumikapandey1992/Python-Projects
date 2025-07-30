# Step 1 – Why we need getters and setters in the first place
# Step 2 – Traditional getter/setter methods
# Step 3 – @property and @<property>.setter as the cleaner alternative
# Real-World Example: Circle Area Calculation

#keywords : getter, setter, @property, @<property>.setter

class BankAccount:
    def __init__(self,balance):
        self._balance = balance  

    # getter method
    @property
    def balance(self):
        return self._balance
    
    #setter method
    @balance.setter
    def balance(self,value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value
    
acc = BankAccount(100)
print(acc.balance)
acc.balance = 200
print(acc.balance)
