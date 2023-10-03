from random import randint


class Player:
    def __init__(self, choice):
        self.choice = choice

    @classmethod
    def create_human(cls, choice):
        return cls(Player.convert(choice))

    def convert(param):
        if param == "1":
            return "rock"
        elif param == "2":
            return "paper"
        elif param == "3":
            return "scissor"

    @classmethod
    def create_robot(cls):
        choice = str(randint(1, 3))
        return cls(Player.convert(choice))

    def rock(self):
        if self.choice == "rock":
            return "Tie"
        if self.choice == "paper":
            return "Lost"
        elif self.choice == "scissor":
            return "Won"

    def paper(self):
        if self.choice == "rock":
            return "Won"
        if self.choice == "paper":
            return "Tie"
        elif self.choice == "scissor":
            return "Lost"

    def scissor(self):
        if self.choice == "rock":
            return "Lost"
        if self.choice == "paper":
            return "Won"
        elif self.choice == "scissor":
            return "Tie"
