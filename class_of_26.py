"""Importing os for cleaning terminal"""

import os


def clear():
    """clearing terminal"""
    os.system("cls")  # windows
    os.system("clear")  # linux


class Game:
    """class game, that runs everything"""

    def __init__(self):
        self.self = self

    def pick_a_choice(self, a, b, c):
        """pick a choice in game"""
        print(
            "\n\033[35mVyberte si mezi těmito možnostmi: "
            f"\033[0m\n \033[31m{a}\033[0m \033[32m{b}\033[0m \033[34m{c}\033[0m"
        )
        answer = input("Napište a, b nebo c: \n")
        return answer

    def next_dialogue(self):
        """Next dialogue in game, only ends when we ENTER"""
        print("\n\033[34mPro pokrok, zmáčkněte\033[0m \033[32m[ENTER]\033[0m")
        while True:
            user_input = input()
            if user_input == "":
                break
        clear()

    def starting_credits(self):
        """The main logo of game"""
        print(
            r"""      
  __              ___   ___ ___  _  _   
 /_ |     /\     |__ \ / _ \__ \| || |  
  | |    /  \       ) | | | | ) | || |_ 
  | |   / /\ \     / /| | | |/ /|__   _|
  | |_ / ____ \   / /_| |_| / /_   | |  
  |_(_)_/    \_\ |____|\___/____|  |_|                                       
"""
        )

        print(
            "\nVítejte u hry 1.A 2024, je to textová hra vytvořena studenty SVT2024.\n"
            "Vše v této hře je čistý výmysl a nic není myšleno vážně a shoda"
            "s reálnými postavami je čistě náhodá.\n"
            "Tato hra je doporučena pro publikum 18+ a slouží pouze k zábavě."
        )
        self.next_dialogue()

    def start_of_game(self):
        """Dialogue on the start of the game"""
        print(""" """)
        self.next_dialogue()

    def first_choice(self):
        """Make the first choice of the game"""
        print(""" """)
        answer = self.pick_a_choice("a", "b", "c")
        self.next_dialogue()
        return answer
    # https://www.reddit.com/r/Classof09Game/comments/17uta4i/class_of_09_reup_game_endings_guide/
    # this is the inspiration for this, and the tree works from left is A and right is C middle option is B
    # Main 3 routes
    def route_a(self):
        print("a")

    def route_b(self):
        print("b")

    def route_c(self):
        print("c")

    # Sub routes of 3 main routes
    def route_a_a(self):
        pass

    def route_a_b(self):
        pass

    def route_b_a(self):
        pass

    def route_b_b(self):
        pass

    def route_c_a(self):
        pass

    def route_c_b(self):
        pass

    # Sub routes of sub routes
    def route_a_a_a(self):
        pass

    def route_a_a_b(self):
        pass

    def route_c_a_a(self):
        pass

    def route_c_a_b(self):
        pass

    def route_c_b_a(self):
        pass

    def route_c_b_b(self):
        pass


# There is the start of the program

clear()
game = Game()
game.starting_credits()
game.start_of_game()
answer1 = game.first_choice()

for option in ("a","b","c"):
    if answer1 == option:
        method_name = f"route_{option}"
        method = getattr(game, method_name, None)
        method()
