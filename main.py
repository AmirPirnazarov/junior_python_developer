class File_action:
    def __init__(self, name_file):
        self.name_file = name_file

    def open_file(self):
        file = open(f"{self.name_file}.txt", 'r')
        print("------")
        print("\n", file.read())
        print("------")
        file.close()


while True:
    name_f = input("Введите имя файла \n")
    try:
        file = File_action(name_f)
        file.open_file()
        break
    except FileNotFoundError:
        print(f"Файл под {name_f} - именнем не существует")

