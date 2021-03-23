class Cards:
    """
    Храним все значения для создания карт
    """

    mast = {                                          #Существующие масти
        "Буба": 'Буба',
        "Чирва": 'Чирва',
        "Кресте": 'Кресте',
        "Пика": 'Пика',
    }

    colour = {                                        #Существующие цвета карт для игры UNO
        "Желтый": 'Желтая',
        "Красный": 'Красная',
        "Синий": 'Синяя',
        "Зеленый": 'Зеленая',
    }

    znach = {                                         #Cуществующие значения карт для всех игр
        "Смена направления": 'Смена_направления',
        "+2": 'Плюс_Две',
        "Пропуск хода": 'Пропуск_хода',
        "Ноль": '0',
        "Один": '1',
        "Два": '2',
        "Три": '3',
        "Четыре": '4',
        "Пять": '5',
        "Шесть": '6',
        "Семь": '7',
        "Восемь": '8',
        "Девять": '9',
        "Десять": '10',
        "Валет": 'Валет',
        "Дама": 'Дама',
        "Король": 'Король',
        "Туз": 'Туз',
    }

    black_aktiv_cards = {                               #Дополнительные значения карт для игры UNO
        "Смена цвета": 'Смена_цвета',
        "Смена цвета + 4": 'Смена цвета_+_4',
    }


class Koloda(Cards):

    import random

    def __init__(self, number):                       #Вводим количество карт
        self.number = number

    koloda = []
    koloda_uno = []

    """
    Проходимся по славорю znach и добавляем к его значениям масти карт из словаря mast.
    Тем самым формируем колоду для игра в Дурака или в БлэкДжек
    """
    def res_koloda(self):
        for v in self.znach.values():
            temp = v + " " + self.mast["Буба"]
            self.koloda.append(temp)                  #добавление карт Буба в колоду
            temp = v + " " + self.mast["Чирва"]
            self.koloda.append(temp)                  #добавление карт Чирва в колоду
            temp = v + " " + self.mast["Кресте"]
            self.koloda.append(temp)                  #добавление карт Кресте в колоду
            temp = v + " " + self.mast["Пика"]
            self.koloda.append(temp)                  #добавление карт Пика в колоду

    """
    В первой функции for создаем по 4 карты "Смена цвета" и "Смена цвета + 4".
    Во второй функции for проходимся по славорю znach и добавляем к его значениям цвета карт из словаря сolour.
    Если в славоре находится 0 то добавляем одну карту, остальные по 2.
    Тем самым формируем колоду для игра в UNO.
    """

    def res_koloda_uno(self):
        for v in self.black_aktiv_cards.values():
            temp = self.black_aktiv_cards["Смена цвета"]
            self.koloda_uno.append(temp)                     #добавление двух карт в колоду
            self.koloda_uno.append(temp)                     #добавление двух карт в колоду, в итоге 4.
            temp = self.black_aktiv_cards["Смена цвета + 4"]
            self.koloda_uno.append(temp)
            self.koloda_uno.append(temp)
        for v in self.znach.values():
            temp = v + " " + self.colour["Желтый"]
            if v in self.znach["Ноль"]:
                self.koloda_uno.append(temp)                  #добавление одной карты 0 в колоду
            else:
                self.koloda_uno.append(temp)                  #добавление двух карт в колоду
                self.koloda_uno.append(temp)                  #добавление двух карт в колоду
            temp = v + " " + self.colour["Красный"]
            if v in self.znach["Ноль"]:
                self.koloda_uno.append(temp)
            else:
                self.koloda_uno.append(temp)
                self.koloda_uno.append(temp)
            temp = v + " " + self.colour["Синий"]
            if v in self.znach["Ноль"]:
                self.koloda_uno.append(temp)
            else:
                self.koloda_uno.append(temp)
                self.koloda_uno.append(temp)
            temp = v + " " + self.colour["Зеленый"]
            if v in self.znach["Ноль"]:
                self.koloda_uno.append(temp)
            else:
                self.koloda_uno.append(temp)
                self.koloda_uno.append(temp)


    """
    Выбор колоды. При вводе пользователем количества карт, формируется колода. Срезы нам немобходимы для првильного 
    вывода карт, т.к. у нас общий словарь значений для всех игр. 
    После среза мы производит перемешивание колоды.
    В цикле создана "защита от дурака", т.е. если пользователь вводит не существующую колоду, ему актоматически
    предлагается сыграть в БлэкДжек
    """

    def vb_koloda(self):                                                #выбор колоды
        if self.number == 36:
            self.res_koloda()
            self.koloda = self.koloda[36::]  # Создание колоды с 36 картами
            self.random.shuffle(self.koloda)  # Перемешивание колоды
            print("Вы выбрали колоду с 36 картами")
            print(self.koloda)
            print(len(self.koloda))
        elif self.number == 52:
            self.res_koloda()
            self.koloda = self.koloda[20::]  # Создание колоды с 52 картами
            self.random.shuffle(self.koloda)
            print("Вы выбрали колоду с 52 картами")
            print(self.koloda)
            print(len(self.koloda))
        elif self.number == 108:
            self.res_koloda_uno()
            self.koloda_uno = self.koloda_uno[:108]  # Создание колоды игры в UNO картами
            self.random.shuffle(self.koloda_uno)
            print("Вы выбрали колоду для игры в UNO с 108 картами")
            print(self.koloda_uno)
            print(len(self.koloda_uno))
        else:
            print("Вы ввели неверное количество карт, поэтому Вам автоматически было предложено сыграть в БлэкДжек")
            print("Выам выдана колода с 52 картами")
            self.res_koloda()
            self.koloda = self.koloda[20::]
            self.random.shuffle(self.koloda)
            print(self.koloda)
            print(len(self.koloda))

k1 = Koloda(106)
k1.vb_koloda()