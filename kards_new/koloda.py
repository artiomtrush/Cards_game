from cards import *

class Koloda(Cards):

    """
    Import random from to shuffle cards
    """
    import random

    def __init__(self): #Enter the name of the Game
        print("Select the game you want to play:\n"
              "1. Durak\n"
              "2. Black Jack\n"
              "3. UNO\n"
              "Enter the game number")
        self.temp = input()
        self.vb_koloda()

    """
    Creating two lists for playing cards. First list for "Durak" and "Black Jack". Second list from "Uno."
    """
    koloda = []
    koloda_uno = []

    """
    Creating is desk for "Durak" and "Black Jack."
    """

    def res_koloda(self):
        for v in self.znach.values():
            for j in self.mast.values():
                self.koloda.append(v + " " + j)

    """
    Creating is desk for "Uno"
    """

    def res_koloda_uno(self):
       self.balck_aktiv_car()
       self.other_cards()

    def balck_aktiv_car(self):
        count = 0
        while count != 8:
            for v in self.black_aktiv_cards.values():
                self.koloda_uno.append(v)
                count += 1

    def other_cards(self):
        for v in self.znach.values():
            for j in self.colour.values():
                if v in self.znach["Ноль"]:
                    self.koloda_uno.append(v + " " + j)
                else:
                    self.koloda_uno.append(v + " " + j)
                    self.koloda_uno.append(v + " " + j)

    """
    Choosing a deck to play. The user chooses a game and, depending on this, a deck is formed.
    If the user selects a non-existing game, the game is automatically displayed to him "Black Jack."
    """

    def vb_koloda(self):
        if self.temp == '1':
            self.res_koloda()
            self.koloda = self.koloda[36::]
            self.random.shuffle(self.koloda)
            print("You have selected a game Durak")

        elif self.temp == '2':
            self.res_koloda()
            self.koloda = self.koloda[20::]
            self.random.shuffle(self.koloda)
            print("You have selected a game Black Jack")

        elif self.temp == '3':
            self.res_koloda_uno()
            self.koloda_uno = self.koloda_uno[:108]
            self.random.shuffle(self.koloda_uno)
            print("You have selected a game UNO")

        else:
            print("You entered a non-existent number. You will play Black Jack")
            self.res_koloda()
            self.koloda = self.koloda[20::]
            self.random.shuffle(self.koloda)