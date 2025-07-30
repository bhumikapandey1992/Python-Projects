# Computer and its inner CPU class

class Computer:
    def __init__(self,brand):
        self.brand = brand
        self.cpu = self.CPU()

    def show(self):
        print(f"Computer Brand: {self.brand}")
        self.cpu.display()

    class CPU:
        def __init__(self):
            self.cores = 4
            self.speed = "3.4GHz"
        
        def display(self):
            print(f"CPU: {self.cores} cores,  {self.speed}")
    
comp = Computer("Dell")
comp.show()