import json
import os
from book.view import View
from book.loadfile import LoadFile
from book.contact import Contact

FILE_PATH = os.path.dirname(os.path.abspath(__file__))


class ContactBook:
    def __init__(self, filepath: str = os.path.join(FILE_PATH, "contact-book.json")) -> None:
        """Инициализация класса
        Args:
            filepath (str): Файл json, в котором хранится все контакты.
        """
        self.filepath = filepath
        self.loadfile = LoadFile(self.filepath)
        self.contacts = None  # целиком все контакты будут тут
        self.view = View()

    def open(self) -> None:
        """Открытие книги контактов"""
        try:
            contacts_dict = json.load(self.loadfile.openfile())
            self.contacts = []
            for i, card in contacts_dict.items():
                self.contacts.append(
                    Contact(card["Name"],
                            card["Number"],
                            card["Description"]
                            )
                )
        except:
            self.view.show_message("Ошибка открытия файл")

    def save(self) -> None:
        """Сохранить контактную книгу"""
        if type(self.contacts) != list:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            contacts_dict = {}
            for i, card in enumerate(self.contacts):
                contacts_dict[i] = card.to_dict()
            self.loadfile.savefile(contacts_dict)
        except:
            self.view.show_message("Ошибка сохранения файл")

    def create(self) -> None:
        """Создать контакт"""
        if type(self.contacts) != list:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            name = input("Введите имя: ")
            number = input("Введите номер: ")
            description = input("Введите описание: ")
            if (len(name) == 0 or len(number) == 0 or len(description) == 0
                    or not number.replace("+", "").isdigit()):
                self.view.show_message("Введены некорректные данные. Повторите попытку.")
            else:
                self.contacts.append(Contact(name, number, description))
                self.save()
                self.view.show_message("Контакт добавлен!")
                return True
        except:
            self.view.show_message("Ошибка создания контакта")

    def find(self) -> None:
        """Найти контакты"""
        if type(self.contacts) != list:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            search = input("Введите поисковое значение: ")
            finded_contacts = []
            for contact in self.contacts:
                if (search.lower() in contact.name.lower() or
                        search.lower() in contact.number or
                        search.lower() in contact.description.lower()):
                    finded_contacts.append(contact)
            if finded_contacts:
                self.view.show_message("Поиск по значению '%s'" % search)
                self.view.show_contacts(finded_contacts)
            else:
                self.view.show_message("Ничего не найдено")
        except:
            self.view.show_message("Ошибка в поиске контакта")

    def edit(self) -> None:
        """Изменить контакт"""
        if type(self.contacts) != list:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            self.view.show_message("Изменение контакта.")
            index = int(input("Введите индекс контакта: "))
            if index < 0 or index >= len(self.contacts):
                self.view.show_message("Контакт не найден")
                return
            contact = self.contacts[index]
            self.view.show_contacts([contact])
            self.view.show_message(
                "Какой пункт изменить: 1 - Name, 2 - Number, 3 - Description, 4 - Все пункты"
            )
            n = int(input())
            if n == 1 or n == 4:
                self.contacts[index].name = input("Введите новое имя: ")
            if n == 2 or n == 4:
                self.contacts[index].number = input("Введите новый номер: ")
            if n == 3 or n == 4:
                self.contacts[index].description = input("Введите новое описание: ")
            if (len(self.contacts[index].name) == 0 or
                    len(self.contacts[index].number) == 0 or
                    len(self.contacts[index].description) == 0 or
                    not self.contacts[index].number.replace("+", "").isdigit()):
                self.view.show_message("Введены некорректные данные. Повторите попытку.")
            else:
                self.view.show_message("Контакт успешно изменен")
                self.save()
                return True
        except:
            self.view.show_message("Ошибка в редактировании контакта")

    def delete(self) -> None:
        """Удалить контакт"""
        if type(self.contacts) != list:
            self.view.show_message("Сначала откройте файл")
            return
        try:
            self.view.show_message("Удаление контакта.")
            index = input("Введите индекс контакта: ")
            if not index:
                self.view.show_message("Введены неправильные данные. Повторите попытку.")
                return
            index = int(index)
            if index < 0 or index >= len(self.contacts):
                self.view.show_message("Контакт не найден")
                return
            del self.contacts[index]
            self.save()
            self.view.show_message("Контакт удален")
            return True
        except:
            self.view.show_message("Ошибка удаления контакта")