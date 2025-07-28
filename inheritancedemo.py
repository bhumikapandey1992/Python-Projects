# Inheritance - Inheritance allows us to write code once in a base class, 
#               and then reuse and extend it in other subclasses.

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Manager(Employee):
    def manage_team(self):
        print(f"{self.name} is managing the team.")
class Developer(Employee):
    def write_code(self):
        print(f"{self.name} is writing python code.")
class Intern(Employee):
    def attend_training(self):
        print(f"{self.name} is attending training.")

m = Manager("Alice",25)
m.show_info() #inherited
m.manage_team()
d = Developer("Bob", 21)
d.show_info() #inherited
d.write_code()
i = Intern("Charlie", 20)
i.show_info()
i.attend_training()