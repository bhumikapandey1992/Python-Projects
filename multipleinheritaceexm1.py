# Multiple inheritance : This allows a class to inherit from more than one parent class — 
#                        and it's super useful when your object needs to combine behaviors or properties 
#                        from different sources."


class A:
    def speak(self):
        print("Speaking from A")
class B:
    def speak(self):
        print("Speaking from B")

class C(A,B):
 pass

c = C()
c.speak() # Speaking from A
print(C.__mro__)
