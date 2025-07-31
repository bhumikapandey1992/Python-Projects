class Computer:
    def __init__(self, brand):
        self.brand = brand
        self.cpu = CPU()

    def show(self):
        print(f"Computer: {self.brand}")
        self.cpu.display()

    def __del__(self):
        print("Computer object has been deleted.")

class CPU:
    def __init__(self):
        self.cores = 4
        self.speed = "3.4 GHz"

    def display(self):
        print(f"CPU: {self.cores} cores at {self.speed}")

    def __del__(self):
        print("CPU object has been deleted.")

c = Computer("Dell")
c.show()
del c
