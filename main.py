class File_action:
    def __init__(self, name_file):
        self.name_file = name_file

    def open_file(self):
        file = open(f"{self.name_file}.txt", 'r')
        print("------")
        print("\n", file.read())
        print("------")
        file.close()

    def add_file(self, text):
        file = open(f"{self.name_file}.txt", 'a')
        file.write("\n" + text)
        print("Добавленно!")
        file.close()


def action_on_file():
    while True:
        action = input("какое действие совершить с файлом: \n 1 - Добавить в список \n 2 - Изменить запись в списке"
                       "\n 3 - Удалить из списка \n 4 - Вычесть общую сумму\n 5 - Посмотреть список\n 0 - выход \n")

        if int(action) == 1:
            add_arr = input("Введите то что ходите добавить в список.\n")
            file.add_file(add_arr)
        else:
            print("Я вас не понимаю")


while True:
    name_f = input("Введите имя файла \n")
    try:
        file = File_action(name_f)
        file.open_file()
        action_on_file()
        break
    except FileNotFoundError:
        print(f"Файл под {name_f} - именнем не существует")

