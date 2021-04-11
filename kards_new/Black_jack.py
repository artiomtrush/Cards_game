from koloda import *
import time

class Black_Jack(Koloda):

    import logging


    count = 0  # Counts dealer
    count_1 = 0  # Count first players
    count_2 = 0  # Count second players

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
        for v in self.count.values():
            if v <= 21 and v != 0:
                print("Player with", v, " points win")
            else:
                pass

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

    """
    Game Black Jack.
    """

    def game(self):
        if self.player == '1':
            self.game_alone()

        elif self.player == '2':
            self.game_with_dealer()

    logging.basicConfig(level=logging.DEBUG, filename='Black_JacK.log')



    # def game(self):
    #     print("Введите ставку первого игрока")
    #     money_1 = input()
    #     print("Ставка компьютера")
    #     money = input()
    #     if self.player == '1':
    #         self.first_razdacha()    #раздача карт пользователю
    #         self.nabor_card()
    #         self.obnl_count_1()
    #         self.first_razdacha()    #раздача карт компьютеру
    #         self.algor_ver()
    #         self.algor_ver()
    #         if self.count > self.count_1 and self.count <= 21:
    #             print("Вы проиграли, компьютер победил. У компьютера", self.count, "очков,у Вас",self.count_1,"очков")
    #             print("Компьютер выйграл", money_1, "денег")
    #         elif self.count < self.count_1 and self.count_1 <= 21:
    #             print("Вы выйграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
    #             print("Вы выйграли", money, "денег")
    #         elif self.count <= 21 and self.count_1 > 21:
    #             print("Вы проиграли, компьютер победил. У компьютера", self.count, "очков,у Вас",self.count_1,"очков")
    #             print("Компьютер выйграл", money_1, "денег")
    #         elif self.count > 21 and self.count_1 <= 21:
    #             print("Вы выйграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
    #             print("Вы выйграли", money, "денег")
    #         elif self.count == self.count_1 and self.count < 21 and self.count_1 < 21:
    #             print("Ничия", self.count, "очков,у Вас", self.count_1, "очков")
    #             print("Ваши деньги Вам вернулись")
    #         else:
    #             print("Вы оба проиграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
    #             print("Ваши деньги отправлены на благотварительность")
    #     if self.player == '2':
    #         print("Введите ставку второго игрока")
    #         money_2 = input()
    #         print("Набирает карты Игрок №1")
    #         self.first_razdacha()    #раздача карт пользователю
    #         self.nabor_card()
    #         self.obnl_count_1()
    #         print("Набирает карты Игрок №2")
    #         self.first_razdacha()    #раздача карт втрому пользователю
    #         self.nabor_card()
    #         self.obnl_count_2()
    #         print("Набирает карты Компьютер")
    #         self.first_razdacha()    #раздача карт компьютеру
    #         self.algor_ver()
    #         self.algor_ver()
    #         if self.count <= 21 and self.count > self.count_1 and self.count > self.count_2:
    #             print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
    #         elif self.count <= 21 and self.count > self.count_1 and self.count_2 > 21:
    #             print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
    #         elif self.count <= 21 and self.count > self.count_2 and self.count_1 > 21:
    #             print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
    #         elif self.count <= 21 and self.count_1 > 21 and self.count_2 > 21:
    #             print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
    #         elif self.count_1 <= 21 and self.count_1 > self.count and self.count_1 > self.count_2:
    #             print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money) + int(money_2), "Денег")
    #         elif self.count_1 <= 21 and self.count_1 > self.count_2 and self.count > 21:
    #             print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money) + int(money_2), "Денег")
    #         elif self.count_1 <= 21 and self.count_1 > self.count and self.count_2 > 21:
    #             print("Игрок 1 победил", self.count_1, "Компьютер", self.count, "очков", "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money) + int(money_2), "Денег")
    #         elif self.count_1 <= 21 and self.count_1 > 21 and self.count > 21:
    #             print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
    #             print("Компьютер выйграл", int(money) + int(money_2), "Денег")
    #         elif self.count_2 <= 21 and self.count_2 > self.count and self.count_2 > self.count_1:
    #             print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
    #             print("Компьютер выйграл", int(money) + int(money_1), "Денег")
    #         elif self.count_2 <= 21 and self.count_2 > self.count_1 and self.count > 21:
    #             print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
    #             print("Компьютер выйграл", int(money) + int(money_1), "Денег")
    #         elif self.count_2 <= 21 and self.count_2 > self.count and self.count_1 > 21:
    #             print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
    #             print("Компьютер выйграл", int(money) + int(money_1), "Денег")
    #         elif self.count_2 <= 21 and self.count > 21 and self.count_1 > 21:
    #             print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
    #             print("Компьютер выйграл", int(money) + int(money_1), "Денег")
    #         else:
    #             print("Вы все проиграли", "Компьютер", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)

b1 = Black_Jack()

