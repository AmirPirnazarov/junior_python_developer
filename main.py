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

    def change_fiel(self, number_line, change_text):
        file = open('a.txt', 'r')
        lines = file.readlines()
        file.close()
        file = open('a.txt', 'r')
        filedata = file.read()
        file.close()
        number_line = number_line - 1
        text_1 = lines[number_line]
        filedata = filedata.replace(text_1, f"{change_text}\n")
        file = open('a.txt', 'w')
        file.write(filedata)


def action_on_file():
    while True:
        action = input("какое действие совершить с файлом: \n 1 - Добавить в список \n 2 - Изменить запись в списке"
                       "\n 3 - Удалить из списка \n 4 - Вычесть общую сумму\n 5 - Посмотреть список\n 0 - выход \n")

        if int(action) == 1:
            add_arr = input("Введите то что ходите добавить в список.\n")
            file.add_file(add_arr)

        elif int(action) == 2:
            number_line = input("Введите какую строку хотитие изменить.\n")
            text_change = input("Введите текст\n")
            file.change_fiel(int(number_line), text_change)
            print("Изменнно!")

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

