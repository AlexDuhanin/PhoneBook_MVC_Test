from book.contact import Contact
from typing import Any

class View:
    MENU_ITEMS = (
        "открыть файл",
        "сохранить файл",
        "показать контакты",
        "создать контакт",
        "найти контакт",
        "изменить контакт",
        "удалить контакт",
        "выход"
    )

    @staticmethod
    def show_menu() -> None:
        """Вывести меню"""
        text = "Введите число действия:\n\n"
        for i, item in enumerate(View.MENU_ITEMS):
            text += f"{i}. {item}\n"
        print(text)

    @staticmethod
    def show_contacts(contacts: list[Contact]) -> None:
        """Показать все контакты
        Args:
            contacts (list[Contact]) : Контакты, которые необходимо вывести в консоли
        """
        if not contacts:
            print("Сначала откройте файл")
        else:
            txt = "" # Контакты:\n
            for i, contact in enumerate(contacts):
                txt += f"{i}. {str(contact)}\n"
            print(txt)

    @staticmethod
    def show_message(msg: Any) -> None:
        """Вывести сообщение"""
        print(msg)