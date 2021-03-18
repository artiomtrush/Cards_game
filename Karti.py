class Cards:
    import random

    def __init__(self, number):                       #будем вводить количество карт
        self.number = number

    mast = {                                          #существующие масти
        "Buba" : 'Буда',
        "Chirva": 'Чирва',
        "Kreste": 'Крест',
        "Pika": 'Пика',
    }

    znach = {                                         #существующие значения карт
        "Два": '2',
        "Три": '3',
        "Четыре": '4',
        "Пять": '5',
        "Шесть" : '6',
        "Семь": '7',
        "Восемь": '8',
        "Девять": '9',
        "Десять": '10',
        "Валет": 'Валет',
        "Дама": 'Дама',
        "Король": 'Король',
        "Туз": 'Туз',
    }

    ochki = {
        "Два": 2,
        "Три": 3,
        "Четыре": 4,
        "Пять": 5,
        "Шесть": 6,
        "Семь": 7,
        "Восемь": 8,
        "Девять": 9,
        "Десять": 10,
        "Валет": 2,
        "Дама": 3,
        "Король": 4,
        "Туз": 11,
    }

class Koloda(Cards):

    koloda = []

    def res_koloda(self):
        for v in self.znach.values():
            temp = v + " " + self.mast["Buba"]
            self.koloda.append(temp)                  #добавление карт буба в колоду
            temp = v + " " + self.mast["Chirva"]
            self.koloda.append(temp)                  #добавление карт чирва в колоду
            temp = v + " " + self.mast["Kreste"]
            self.koloda.append(temp)                  #добавление карт чирва в колоду
            temp = v + " " + self.mast["Pika"]
            self.koloda.append(temp)                  #добавление карт пика в колоду

    def vb_koloda(self):                              # выбор колоды
        if self.number == 36:
            self.koloda = self.koloda[16::]           #создание колоды с 36 картами
            print("Вы выбрали колоду с 36 картами")
        elif self.number == 52:
            print("Вы выбрали колоду с 52 картами")
        else:
            print("Колоды с данным количеством карт не существует")
            self.koloda = 0

    def perem_koloda(self):                           #перемешивание колоды
        self.res_koloda()
        self.vb_koloda()
        self.random.shuffle(self.koloda)

#k1 = Koloda(36)
#k1.res_koloda()
#k1.vb_koloda()
#k1.perem_koloda()

class Ochko_21(Koloda):

    count = 0                                        #счетчик очков в игре

    def __init__(self, number):                       #ввод количества карт в колоде, количества игроков
        super().__init__(number)

    def y(self):
        self.koloda.pop()

    def n(self):
        return 0

    def vid_kart(self):
        super().perem_koloda()                         #перемешивание колоды
        input()
        if input() == y:
            temp = self.y()
            self.count += temp
            print("У вас", self.count, "очков")
        else:
            print("У вас", self.count, "очков")


d1 = Ochko_21(36,2)
d1.vid_kart()







