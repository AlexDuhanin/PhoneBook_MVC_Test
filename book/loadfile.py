import json
from book.view import View
import io

class LoadFile:

    def __init__(self, filepath: str) -> None:
        """Инициализация класса
        Args:
            filepath (str): Путь до файла json, в котором лежат контакты.
        """
        self.filepath = filepath
        self.view = View()

    def openfile(self) -> io.TextIOWrapper:
        """Открытие файла"""
        file = open(self.filepath, "r", encoding="utf-8")
        self.view.show_message("Файл открыт")
        return file

    def savefile(self, book: dict) -> None:
        """Сохранение файла
        Args:
            book (dict): Все контакты в формате словаря.
        """
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(book, file, indent=4, ensure_ascii=False)
        self.view.show_message("Файл сохранен")