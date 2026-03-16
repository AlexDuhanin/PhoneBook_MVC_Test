from book.view import View
from book.contactbook import ContactBook


class Controller:

    def __init__(self) -> None:
        """Инициализация класса"""
        self.book = ContactBook()
        self.view = View()

    def run(self) -> None:
        """Главный цикл работы программы"""
        while True:
            self.view.show_menu()

            try:
                n = int(input("Ввод: "))
            except ValueError:
                self.view.show_message("Ошибка ввода")

            if n == 0:
                self.book.open()
            elif n == 1:
                self.book.save()
            elif n == 2:
                self.view.show_contacts(self.book.contacts)
            elif n == 3:
                self.book.create()
            elif n == 4:
                self.book.find()
            elif n == 5:
                self.book.edit()
            elif n == 6:
                self.book.delete()
                self.book.save()
            elif n == 7:
                self.view.show_message("Выход из телефонной книжки")
                break


if __name__ == "__main__":
    controller = Controller()
    controller.run()
