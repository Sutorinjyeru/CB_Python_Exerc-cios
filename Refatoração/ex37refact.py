from random import randint

from ex37class import Player


def main():
    p1_choice = ""
    p2_choice = ""
    while True:
        mode = input("Gamemode(1/2)")
        while True:
            try:
                if mode == "1":
                    player_choice(p1_choice, 2)
                    player_choice(p2_choice, 1)
                elif mode == "2":
                    p2 = Player.create_robot()
                elif mode == "3":
                    break
                try_again(mode)
            except ValueError:
                ("Deu rui ")
                continue
            else:
                break

        p2 = Player.create_human(p2_choice)
        p1 = Player.create_human(p1_choice)

        if p1.choice == "rock":
            print(Player.rock(p2))
        elif p1.choice == "paper":
            print(Player.paper(p2))
        elif p1.choice == "scissor":
            print(Player.scissor(p2))


def try_again(param):
    if param != "1" or param != "2" or param != "3":
        raise ValueError


def player_choice(param, x):
    while True:
        try:
            param = input(f"{x}Choice(rock,paper,scissor)")
            try_again(param)
        except ValueError:
            print("PUTZ")
            continue
        else:
            return param


if __name__ == "__main__":
    main()
