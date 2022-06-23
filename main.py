class File_action:
    def __init__(self, name_file):
        self.name_file = name_file  # Принимает имя файла

    def open_file(self):  # функция открытии файла
        file = open(f"{self.name_file}.txt", 'r')  # Открываем файл
        print("--- Начало списка ---")
        print("\n", file.read())   # выводим список
        print("--- Конец списка ---\n")
        file.close()

    def add_file(self, text):  # Добавление в конец списка
        file = open(f"{self.name_file}.txt", 'a')
        file.write("\n" + text)
        print("Добавленно!")
        file.close()

    def delate_file(self, namber_line):  # Удаление строки из списка
        file = open('a.txt', 'r')
        lines = file.readlines()
        file.close()
        file = open('a.txt', 'r')
        filedata = file.read()
        file.close()
        number = namber_line - 1  # номер строки которую вводит пользователь отнимаем 1 потому что список начин с 0
        text_1 = lines[number]
        filedata = filedata.replace(text_1, "")  # меняем строку на пустую
        file = open('a.txt', 'w')
        file.write(filedata)

    def change_fiel(self, number_line, change_text):  # меняем строку на другую
        file = open('a.txt', 'r')
        lines = file.readlines()
        file.close()
        file = open('a.txt', 'r')
        filedata = file.read()
        file.close()
        number_line = number_line - 1
        text_1 = lines[number_line]
        filedata = filedata.replace(text_1, f"{change_text}\n") # Меняем строку на ту что ввел пользователь
        file = open('a.txt', 'w')
        file.write(filedata)

    def total_amount(self):  # Вычислить общ кол-во
        file = open('a.txt', 'r')
        lines = file.readlines()  # читаем файл по строкам
        file.close()
        s = []  # создаем пустой список
        for i in lines:
            for t in i.split():  # Выводим только цыфры
                try:
                    s.append(int(t))  # С помошью вложенного цылка выбираем только цыфры и доб в список
                except ValueError:
                    pass
        print("общую сумму равна:", sum(s), "\n")


def action_on_file():  # Функция которая принимает действие
    while True:  # бесконечный цыкл
        action = input("какое действие совершить с файлом: \n 1 - Добавить в список \n 2 - Изменить запись в списке"
                       "\n 3 - Удалить из списка \n 4 - Вычесть общую сумму\n 5 - Посмотреть список\n 0 - выход \n")

        if int(action) == 1:
            add_arr = input("Введите то что ходите добавить в список.\n")
            file.add_file(add_arr)

        elif int(action) == 2:
            while True:
                number_line = input("Введите какую строку хотитие изменить.\n")
                if number_line.isdigit():  # Проверяем стока состоит только из цыфр?
                    try:
                        text_change = input("Введите текст\n")
                        file.change_fiel(int(number_line), text_change)  # Метод принимает 2 аргумента номер строки и те
                        print("Изменнно!\n")
                        break
                    except IndexError:
                        print("Вы вводите номер строки которого нет в файле!\n")
                else:
                    print("Вы ввели что то не то\n")

        elif int(action) == 3:
            while True:
                number_line = input("Выберете какую строку хотитие удалить.\n")
                if number_line.isdigit():  # Проверяем стока состоит только из цыфр?
                    try:
                        file.delate_file(int(number_line))
                        print("Удаленно!\n")
                        break
                    except IndexError:
                        print("Вы вводите номер строки которого нет в файле!\n")
                else:
                    print("Вы ввели что то не то\n")

        elif int(action) == 4:
            file.total_amount()

        elif int(action) == 5:
            file.open_file()

        elif int(action) == 0:
            exit(0)
        else:
            print("Я вас не понимаю")


while True:  # Бесконечный цыкл
    name_f = input("Введите имя файла \n")
    try:  # проверяем на исключение
        file = File_action(name_f)  # создаем обьект
        file.open_file()  # Вызываем метод открытия файла
        action_on_file()  # После открытия переходим к функции action_on_file()
        break
    except FileNotFoundError:
        print(f"Файл под {name_f} - именнем не существует")