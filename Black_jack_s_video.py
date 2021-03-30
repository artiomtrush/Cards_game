class Cards:
    """
    Храним все значения для создания карт
    """
    mast = {  # Существующие масти
        "Буба": 'Буба',
        "Чирва": 'Чирва',
        "Кресте": 'Кресте',
        "Пика": 'Пика',
    }

    colour = {  # Существующие цвета карт для игры UNO
        "Желтый": 'Желтая',
        "Красный": 'Красная',
        "Синий": 'Синяя',
        "Зеленый": 'Зеленая',
    }

    znach = {  # Cуществующие значения карт для всех игр
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

    black_aktiv_cards = {  # Дополнительные значения карт для игры UNO
        "Смена цвета": 'Смена_цвета',
        "Смена цвета + 4": 'Смена цвета_+_4',
    }


class Koloda(Cards):
    """
    Импортируем рандом для возможности перемешивания карт
    """
    import random

    def __init__(self, number):  # Вводим количество карт
        self.number = number

    """
    Создаем две колоды. Потому что в одной карты хранятся по мастям, а во второй по цветам.
    Первая для игры в 21 либо БлэкДжек.
    Вторая для игры в UNO.
    """
    koloda = []
    koloda_uno = []

    """
    Проходимся по славорю znach и добавляем к его значениям масти карт из словаря mast.
    Тем самым формируем колоду для игра в Дурака или в БлэкДжек
    """

    def res_koloda(self):
        for v in self.znach.values():
            temp = v + " " + self.mast["Буба"]
            self.koloda.append(temp)  # Добавление карт Буба в колоду
            temp = v + " " + self.mast["Чирва"]
            self.koloda.append(temp)  # Добавление карт Чирва в колоду
            temp = v + " " + self.mast["Кресте"]
            self.koloda.append(temp)  # Добавление карт Кресте в колоду
            temp = v + " " + self.mast["Пика"]
            self.koloda.append(temp)  # Добавление карт Пика в колоду

    """
    В первой функции for создаем по 4 карты "Смена цвета" и "Смена цвета + 4".
    Во второй функции for проходимся по славорю znach и добавляем к его значениям цвета карт из словаря сolour.
    Если в славоре находится 0 то добавляем одну карту, остальные по 2.
    Тем самым формируем колоду для игра в UNO.
    """

    def res_koloda_uno(self):
        for v in self.black_aktiv_cards.values():
            temp = self.black_aktiv_cards["Смена цвета"]
            self.koloda_uno.append(temp)  # Добавление двух карт в колоду
            self.koloda_uno.append(temp)  # Добавление двух карт в колоду, в итоге 4.
            temp = self.black_aktiv_cards["Смена цвета + 4"]
            self.koloda_uno.append(temp)
            self.koloda_uno.append(temp)
        for v in self.znach.values():
            temp = v + " " + self.colour["Желтый"]
            if v in self.znach["Ноль"]:
                self.koloda_uno.append(temp)  # Добавление одной карты 0 в колоду
            else:
                self.koloda_uno.append(temp)  # Добавление двух карт в колоду
                self.koloda_uno.append(temp)  # Добавление двух карт в колоду
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

    def vb_koloda(self):  # выбор колоды
        if self.number == 36:
            self.res_koloda()
            self.koloda = self.koloda[36::]  # Создание колоды с 36 картами
            self.random.shuffle(self.koloda)  # Перемешивание колоды
            print("Вы выбрали колоду с 36 картами")
        elif self.number == 52:
            self.res_koloda()
            self.koloda = self.koloda[20::]  # Создание колоды с 52 картами
            self.random.shuffle(self.koloda)
            print("Вы выбрали колоду с 52 картами")
        elif self.number == 108:
            self.res_koloda_uno()
            self.koloda_uno = self.koloda_uno[:108]  # Создание колоды игры в UNO картами
            self.random.shuffle(self.koloda_uno)
            print("Вы выбрали колоду для игры в UNO с 108 картами")
        else:
            print("Вы ввели неверное количество карт, поэтому Вам автоматически было предложено сыграть в БлэкДжек")
            print("Вам выдана колода с 52 картами")
            self.res_koloda()
            self.koloda = self.koloda[20::]
            self.random.shuffle(self.koloda)


class Black_Jack(Koloda):

    """
     Функция воспроизведения видео
     """

    def video(self):

        import pyglet

        vidPath = '/home/artiom/TeachMeSkills/kards/file.mp4'
        window = pyglet.window.Window()
        player = pyglet.media.Player()
        source = pyglet.media.StreamingSource()
        MediaLoad = pyglet.media.load(vidPath)

        player.queue(MediaLoad)
        player.play()

        @window.event
        def on_draw():
            if player.source and player.source.video_format:
                player.get_texture().blit(50, 50)

        pyglet.app.run()



    count = 0  # Счетчик очков в игре компьютера
    count_1 = 1  # Счетчик очков в игре первого пользователя
    count_2 = 2  # Счетчик очков в игре второго пользователя

    """
     Функции присваивания значения одного счетчика другому, замет обнуляет первый. Сделано для того чтобы не 
     переписыват отдельно функцию поиска очков. 
     """

    def obnl_count_1(self):
        self.count_1 = self.count
        self.count = 0

    def obnl_count_2(self):
        self.count_2 = self.count
        self.count = 0

    """
    Словарь со значением карт и их весом, т.е. очками за карту.
    """

    ochki = {  # Очки в игре
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

    """
    Наследование вводимых числа вводимых карт
    """

    def __init__(self, number, player):  # Ввод количества карт в колоде и числа игроков
        super().__init__(number)
        self.player = player


    """
    Наследование функции создания и переменшивания колоды
    """

    def vid_kart(self):
        super().vb_koloda()  # Перемешивание колоды

    """
    Функция выдачи карты с колоды. При выдаче с колобы, данная карта убирается из нашего списка, чтобы ее нельзя
    было использовать второй раз. Затем по первому слову(значению карты) ищет данный вес карты в словаре
    значения (т.к. для нас не важна масть карты, а важно значение карты). После поиска прибавляет значение к счетчику.
    """

    def ochki_card(self):  # Выдача карты с колоды и поиск веса
        self.a = self.koloda.pop()
        print("Ваша карта", self.a)
        self.temp_2 = self.a.split(" ")[0]
        self.search_ochki()
        self.result()

    """
    Функция поиска очков карт и добавление ее веса к счетчику.
    Ищет ключ в словаре, затем преобрадует строку в число и добавляет число к счетчику.
    Если находит Туз, то спрашивает что использовать 1 или 11
    """

    def search_ochki(self):  # Функция поиска веса карты в значениях
        if self.temp_2 in self.ochki.keys():  # Поиск значения в словаре
            self.x = self.ochki[self.temp_2]  # Присваивание временному значению веса карты
            self.x = int(self.x)  # Преобразование из строки в число
            if self.x == 11:
                print("Вы хотите использовать Туз как 11 или 1")
                self.x = input() # Ввод 11 или 1
            self.count += int(self.x)  # Добавление веса карты к счетчику очков
        else:
            pass


    """
    Функция контроля счета. Проверяет текущий счет пользователя. Если у него меньше 21 очка, предлагает набрать еще.
    Если у пользователя 21 очко - поздравляет его с победой.
    Если у пользователя больше 21 очка - объявлет о его проигрыше.
    """

    def result(self):
        if self.count < 21:
            print("У Вас", self.count, "очка(в)")
        elif self.count == 21:
            print("У Вас", self.count, "очка(в)")
        else:
            print("У Вас", self.count, "очка(в)")


    """
    Функция донабора карт. При вводе пользователем слова "да". Выдает одну карту с колоды, идет ее значение и выдает
    вес карты. При вводе пользователем слова "нет", выдает текущий счет его очков.
    """

    def nabor_card(self):
        print("Вы хотите набрать еще карт?")
        print("Вводите да для набора карт, для выхода введите нет")
        while input() == "да":
            self.ochki_card()
        else:
            print("У Вас", self.count, "очков")

    """
    Функция первой раздачи. При первой раздаче выдает две карты, текущий счет очков, Спрашивает необходим ли донабор 
    карт при помощи вызова функции набор карт.
    """

    def first_razdacha(self):
        self.ochki_card()
        self.ochki_card()

    """
    Алгоритм просчета вероятноти для компьютера. Пользователь сам будет выбирать брать ему карту или нет.
    """

    def algor_ver(self):
        if 21 - self.count > 11:
            self.ochki_card()
        elif 21 - self.count >= 5:
            self.ochki_card()
        else:
            pass


    def game(self):
        self.vid_kart()
        print("Введите ставку первого игрока")
        money_1 = input()
        print("Ставка компьютера")
        money = input()
        if self.player == 1:
            self.first_razdacha()    #раздача карт пользователю
            self.nabor_card()
            self.obnl_count_1()
            self.first_razdacha()    #раздача карт компьютеру
            self.algor_ver()
            self.algor_ver()
            if self.count > self.count_1 and self.count <= 21:
                print("Вы проиграли, компьютер победил. У компьютера", self.count, "очков,у Вас",self.count_1,"очков")
                print("Компьютер выйграл", money_1, "денег")
                self.video()
            elif self.count < self.count_1 and self.count_1 <= 21:
                print("Вы выйграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
                print("Вы выйграли", money, "денег")
            elif self.count <= 21 and self.count_1 > 21:
                print("Вы проиграли, компьютер победил. У компьютера", self.count, "очков,у Вас",self.count_1,"очков")
                print("Компьютер выйграл", money_1, "денег")
                self.video()
            elif self.count > 21 and self.count_1 <= 21:
                print("Вы выйграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
                print("Вы выйграли", money, "денег")
                self.video()
            elif self.count == self.count_1 and self.count < 21 and self.count_1 < 21:
                print("Ничия", self.count, "очков,у Вас", self.count_1, "очков")
                print("Ваши деньги Вам вернулись")
                self.video()
            else:
                print("Вы оба проиграли. У компьютера", self.count, "очков,у Вас", self.count_1, "очков")
                print("Ваши деньги отправлены на благотварительность")
                self.video()
        if self.player == 2:
            print("Введите ставку второго игрока")
            money_2 = input()
            print("Набирает карты Игрок №1")
            self.first_razdacha()    #раздача карт пользователю
            self.nabor_card()
            self.obnl_count_1()
            print("Набирает карты Игрок №2")
            self.first_razdacha()    #раздача карт втрому пользователю
            self.nabor_card()
            self.obnl_count_2()
            print("Набирает карты Компьютер")
            self.first_razdacha()    #раздача карт компьютеру
            self.algor_ver()
            self.algor_ver()
            if self.count <= 21 and self.count > self.count_1 and self.count > self.count_2:
                print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
                self.video()
            elif self.count <= 21 and self.count > self.count_1 and self.count_2 > 21:
                print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
                self.video()
            elif self.count <= 21 and self.count > self.count_2 and self.count_1 > 21:
                print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
                self.video()
            elif self.count <= 21 and self.count_1 > 21 and self.count_2 > 21:
                print("Компьютер победил", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money_1) + int(money_2), "Денег")
                self.video()
            elif self.count_1 <= 21 and self.count_1 > self.count and self.count_1 > self.count_2:
                print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money) + int(money_2), "Денег")
                self.video()
            elif self.count_1 <= 21 and self.count_1 > self.count_2 and self.count > 21:
                print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money) + int(money_2), "Денег")
                self.video()
            elif self.count_1 <= 21 and self.count_1 > self.count and self.count_2 > 21:
                print("Игрок 1 победил", self.count_1, "Компьютер", self.count, "очков", "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money) + int(money_2), "Денег")
                self.video()
            elif self.count_1 <= 21 and self.count_1 > 21 and self.count > 21:
                print("Игрок 1 победил", self.count_1, "Компьютер",self.count,"очков", "Игрок 2", self.count_2)
                print("Компьютер выйграл", int(money) + int(money_2), "Денег")
                self.video()
            elif self.count_2 <= 21 and self.count_2 > self.count and self.count_2 > self.count_1:
                print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
                print("Компьютер выйграл", int(money) + int(money_1), "Денег")
                self.video()
            elif self.count_2 <= 21 and self.count_2 > self.count_1 and self.count > 21:
                print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
                print("Компьютер выйграл", int(money) + int(money_1), "Денег")
                self.video()
            elif self.count_2 <= 21 and self.count_2 > self.count and self.count_1 > 21:
                print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
                print("Компьютер выйграл", int(money) + int(money_1), "Денег")
                self.video()
            elif self.count_2 <= 21 and self.count > 21 and self.count_1 > 21:
                print("Игрок 2 победил", self.count_2, "Компьютер",self.count,"очков", "Игрок 1", self.count_1)
                print("Компьютер выйграл", int(money) + int(money_1), "Денег")
                self.video()
            else:
                print("Вы все проиграли", "Компьютер", self.count, "Игрок 1", self.count_1, "Игрок 2", self.count_2)
                self.video()

b1 = Black_Jack(52, 1)
b1.game()
