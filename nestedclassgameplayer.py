# Game with a nested Player class

class Game:
    def __init__(self,title):
        self.title = title
        self.player = self.Player("Alex")

    def start(self):
        print(f"Starting game: {self.title}")
        self.player.display()

    class Player:
        def __init__(self,name):
            self.name = name
            self.level = 1

        def display(self):
            print(f"Player: {self.name}, Level: {self.level}")

game1 = Game("Adventure Quest")
game1.start()