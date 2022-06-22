class File_action:
    def __init__(self, name_file):
        self.name_file = name_file

    def open_file(self):
        file = open(f"{self.name_file}.txt", 'r')
        print("\n", file.read())


name_f = input("Введите имя файла \n")

file = File_action(name_f)
file.open_file()


