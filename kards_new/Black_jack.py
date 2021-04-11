from koloda import *
import time

class Black_Jack(Koloda):

    import logging

    count = 0  # Counts dealer
    count_1 = 0  # Count first players
    count_2 = 0  # Count second players
    count_player = [] # Count all players

    """
     Functions for resetting players` points counters. 
     """

    def res_count_1(self):
        self.count_1 = self.count
        self.count = 0

    def res_count_2(self):
        self.count_2 = self.count
        self.count = 0

    """
    Cards points dictionary.
    """

    ochki = {  # Points game
        "2": '2',
        "3": '3',
        "4": '4',
        "5": '5',
        "6": '6',
        "7": '7',
        "8": '8',
        "9": '9',
        "10": '10',
        "Валет": '10',
        "Дама": '10',
        "Король": '10',
        "Туз": '11',
    }

    def __init__(self):
        super().__init__()
        print("Enter the number of players\n"
              "1. You will play alone\n"
              "2. You will play with dealer\n"
              "3. You will play together\n"
              "4. You will play together with dealer")
        time.sleep(1)
        self.player = input()
        self.logging.debug(f'User enter {self.player}')
        time.sleep(1)
        self.game()


    """
    Function of issuing cards from the desk and getting its value.
    """

    def ochki_card(self):
        time.sleep(1)
        self.a = self.koloda.pop()
        print("Card", self.a)
        self.logging.debug(f'Card gave {self.a}')
        self.temp_2 = self.a.split(" ")[0]
        self.search_ochki()
        time.sleep(1)
        print("Sum points", self.count)
        self.logging.debug(f'Sum points {self.count}')

    """
    Function to search for cards and add value to the count. 
    If the cards is "Туз", you choose as 11 or 1.
    """

    def search_ochki(self):
        if self.temp_2 in self.ochki.keys():
            self.x = int(self.ochki[self.temp_2])
            if self.x == 11:
                print("Use Туз as 11 or 1")
                self.x = input()
                self.logging.debug(f'User enter {self.x}')
            self.count += int(self.x)
        else:
            pass

    """
    Function receive cards.
    """

    def nabor_card(self):
        print("If you`ll give card enter y\n"
              "Press any other letter to exit")
        while input() == "y":
            self.ochki_card()
        else:
            print("You gave", self.count, "points")

    """
    Function first receive cards. Player(s) or dealer.
    """

    def first_razdacha(self):
        self.ochki_card()
        self.ochki_card()

    """
    Actions dealer.
    """
    def algor_ver(self):
        if 21 - self.count > 11:
            self.ochki_card()
        elif 21 - self.count >= 5:
            self.ochki_card()
        else:
            pass

    """
    Function search winner.
    """
    def search_win(self):
        if self.player == '1':
            if self.count > 21:
                print("You lost your money. Your bet were", self.money_1, "cash.")

        else:
            for num in self.count, self.count_1, self.count_2:
                if num <= 21 and num != 0:
                    self.count_player.append(num)
                else:
                    pass
            print("Player with", max(self.count_player), "points win.")

            "Надо добавить ссумарный счет выйгранных денег"

    """
    Game play alone.
    """

    def game_alone(self):
        print("Enter your bet")
        self.money_1 = input()
        time.sleep(1)
        self.first_razdacha()
        time.sleep(1)
        self.nabor_card()
        self.search_win()

    """
    Game dealer.
    """

    def game_dealer(self):
        print("Dealer bet", self.money_1, "points.")
        self.money = self.money_1
        self.first_razdacha()
        self.algor_ver()
        self.algor_ver()


    """
    Game play with dealer.
    """

    def game_with_dealer(self):
        self.game_alone()
        self.res_count_1()
        self.game_dealer()
        print("Player has", self.count_1,"points\n"
                                       "Dealer has", self.count,"points.")
        self.search_win()

    """
    Game Black Jack.
    """

    def game(self):
        if self.player == '1':
            self.game_alone()

        elif self.player == '2':
            self.game_with_dealer()

    logging.basicConfig(level=logging.DEBUG, filename='Black_JacK.log')

    "1. При запуске игры с компрьютером два раза происходит выполнение операции победителя"
    "2. Дописать действия при 3 -4"
    "3. Подключить видео"
    "4. Переделать алгоритм компьюетра через while true"
    "5. Добавить в логи время"

b1 = Black_Jack()

