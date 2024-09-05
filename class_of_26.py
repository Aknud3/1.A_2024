import os

clear = lambda: os.system("cls")


class Game:
    def __init__(self):
        self.self = self

    def pick_a_choice(self, a, b, c):
        print(f"\n\033[35mVyberte si mezi těmito možnostmi: \033[0m\n \033[31m{a}\033[0m \033[32m{b}\033[0m \033[34m{c}\033[0m")
    
    def next_dialogue(self):
        print("\n\033[34mPro pokrok, zmáčkněte\033[0m \033[32m[ENTER]\033[0m")
        while True:
            user_input = input()
            if user_input == "":
                break
        clear()

    
    def starting_credits(self):
        print(" __  __       _                         _   _   ___   ___ ___   __  ")
        print("|  \/  |     | |                       | | (_) |__ \ / _ \__ \ / /  ")
        print("| \  / | __ _| |_ _   _ _ __ __ _ _ __ | |_ _     ) | | | | ) / /_  ")
        print("| |\/| |/ _` | __| | | | '__/ _` | '_ \| __| |   / /| | | |/ / '_ \ ")
        print("| |  | | (_| | |_| |_| | | | (_| | | | | |_| |  / /_| |_| / /| (_) |")
        print("|_|  |_|\__,_|\__|\__,_|_|  \__,_|_| |_|\__|_| |____|\___/____\___/ ")
        print(
            f"\nVítejte u hry Maturanti 2026, je to textová hra vytvořena studenty SVT2024.\n"
            f"Vše v této hře je čistý výmysl a nic není myšleno vážně a shoda s reálnými postavami je čistě náhodá.\n"
            f"Tato hra je doporučena pro publikum 18+ a slouží pouze k zábavě."
        )
        self.next_dialogue()


    def start_of_game(self):
        print(
            f"""Je to vtipné, když holka říká svůj příběh...
A jen jí řeknou, že je to nereálné
Téměř jako by se báli uvěřit, že je to SKUTEČNÉ.
Pro všechny, kdo to nevědí...
Moje máma je SVINĚ, můj táta se zastřelil, můj život je na houby,
A můj brácha je na SEZNAMU sledovaných.
Ne nutně v tomhle pořadí... nebo možná, já nevím.
Ale minulý rok...
Mě tahle kombinace dostala na tu NEJHORŠÍ, nejnebezpečnější školu, co si jde představit.
Aspoň jsem si to myslela.
Pak jsem mluvila s ostatními a ukázalo se, že to nebylo tak hrozné?
No, ne, BYLO to tak hrozné, jen to bylo docela standardní.
Jiné holky říkaly, že jejich tělocvikář s nimi chtěl spát, jejich poradce jim psal na Teamsy ve 3 ráno.
Já byla jediná, kdo měl za učitele fotografa, který byl bílý nácek. Takže to bylo aspoň něco...
ALE TADY JE PROBLÉM:
Máma neposlouchá,
ředitelce je to JEDNO, a já mám ještě CELÝ poslední ročník před sebou.
Můj život je jen hra, nemocná a beznadějná hra.
Nikdy jsem nebyla nějak zvlášť „věřící“, ale jestli je Bůh nějaká introvertní nula sedící u svého počítače...
Opravdu doufám, že mi může pomoci tohle zvládnout."""
        )
        self.next_dialogue()


clear()
game = Game()
game.starting_credits()
game.start_of_game()
