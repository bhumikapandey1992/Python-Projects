class Pilot:
    def fly_plane(self):
        print("Flying a plane high above the clouds.")
class Lifeguard:
    def save_swimmer(self):
        print("Saving someone from drowning.")
    
# Subclass inheriting from both parent classes
class SuperPerson(Pilot,Lifeguard):
    def multitask(self):
        print("I can both fly and save lives.")

# create an object
hero = SuperPerson()

# Call methods from both parent classes
hero.fly_plane() # From Pilot
hero.save_swimmer() # From Lifeguard class
hero.multitask() # From SuperPerson