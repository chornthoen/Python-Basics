class Game:
    def __init__(self, type, your_number, machine_name):
        self.y_n = your_number
        self.t = type
        self.m = machine_name


class GamePlay(Game):
    def __init__(self, id, name, type, your_number, machine_name):
        super().__init__(type, your_number, machine_name)
        self.id = id
        self.name = name

    def display(self):

        print("ID =", self.id, " ,Name =", self.name,
              " ,Type =", self.t, " ,Your Number =", self.y_n,
              " ,Machine Name =", self.m)


game = GamePlay(1, "dara", "ABC", 12, "Mama")
game.display()
