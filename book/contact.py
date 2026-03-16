class Contact:
    def __init__(self, name: str, number: str, description: str) -> None:
        """Инициализация класса
        Args:
            name (str) : Имя контакта.
            number (str) : Номер контакта.
            description (str) : Описание контакта.
        """
        self.name = name
        self.number = number
        self.description = description

    def to_dict(self) -> dict[str, str]:
        """Возвращает данные карточки контакта в формате словаря"""
        return {
            "Name": self.name,
            "Number": self.number,
            "Description": self.description
        }

    def __str__(self) -> str:
        return f"{self.name} | {self.number} | {self.description}"