"""Importing os and platform for cleaning terminal"""

import os
import platform


def clear():
    """clearing terminal"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


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
    # this is the inspiration for this, A left, C right, B middle
    # Main 3 routes

    def route_a(self):
        """this is the first road"""
        answer = self.pick_a_choice("a", "b", "c")
        self.next_dialogue()
        return answer

    def route_b(self):
        """second main road"""

    def route_c(self):
        """third main road"""

    # Sub routes of 3 main routes
    def route_a_a(self):
        """first part of main road a"""
        print("haha")

    def route_a_b(self):
        """second part of main road a"""

    def route_b_a(self):
        """first part of main road b"""

    def route_b_b(self):
        """second part of main road b"""

    def route_c_a(self):
        """first part of main road c"""

    def route_c_b(self):
        """second part of main road c"""

    # Sub routes of sub routes
    def route_a_a_a(self):
        """first part of first part of main road a"""

    def route_a_a_b(self):
        """second part of first part of main road a"""

    def route_c_a_a(self):
        """first part of first part of main road c"""

    def route_c_a_b(self):
        """second part of first part of main road c"""

    def route_c_b_a(self):
        """first part of second part of main road c"""

    def route_c_b_b(self):
        """second part of second part of main road c"""


# There is the start of the program

clear()
game = Game()
game.starting_credits()
game.start_of_game()
answer1 = game.first_choice()

options = ["", "", ""]
answers =["", "", ""]
routes =["", "", ""]
route_names = ["", "", ""]


""" Big loop that needs to be tested
for i in range(3):
    for options[i] in ("a", "b", "c"):
        if answers[i] == options[i]:
            if i == 0:
                route_names[i] = f"route_{options[i]}"
                routes[i] = getattr(game, route_names[i], None)
                answers[i+1] = routes[i]()
            else:
                route_names[i] = f"{route_names[i-1]}_{options[i]}"
                routes[i] = getattr(game, route_names[i], None)
                answers[i+1] = routes[i]()
"""                
# working version of logic
        
for option1 in ("a", "b", "c"):
    if answer1 == option1:
        route_name1 = f"route_{option1}"
        route = getattr(game, route_name1, None)
        answer2 = route()
        break

for option2 in ("a", "b", "c"):
    if answer2 == option2:
        route_name2 = f"{route_name1}_{option2}"
        route2 = getattr(game, route_name2, None)
        answer3 = route2()
        break

for option3 in ("a", "b", "c"):
    if answer3 == option3:
        route_name3 = f"{route_name2}_{option3}"
        route3 = getattr(game, route_name3, None)
        route3()
