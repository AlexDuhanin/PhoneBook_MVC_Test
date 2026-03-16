import pytest
from book.contactbook import ContactBook

@pytest.mark.parametrize("name, number, description",
                        [("Иван", "+79998883221", "Друг"),
                        ("Ivan", "+395672383713", "Friend"),
                        ("John", "+7abcdef", "desc"),
                        ("", "", "")])
def test_create_contact(mocker, name, number, description):
    """Тестирование создание контакта"""
    book = ContactBook()
    book.open()
    lenght = len(book.contacts)
    assert type(book.contacts) == list
    mocker_input = mocker.patch('builtins.input', side_effect=[name, number, description])
    result = book.create()
    assert mocker_input.call_count == 3 # вызвался ли мок правильное кол. раз
    if result:
        assert len(book.contacts) == lenght + 1
        assert book.contacts[-1].name == name
        assert book.contacts[-1].number == number
        assert book.contacts[-1].description == description
    else:
        assert len(book.contacts) == lenght


@pytest.mark.parametrize("search_word",
                         ["Иван", "+79998883221", "описание", "123456", "тест неизвестных слов"])
def test_find_contact(mocker, search_word):
    """Тестирование поиска контакта"""
    book = ContactBook()
    book.open()
    assert type(book.contacts) == list
    mocker_input = mocker.patch('builtins.input', return_value=search_word)
    book.find()
    assert mocker_input.call_count == 1


@pytest.mark.parametrize("index, n, name, number, description",
                        [("6", "4", "Иван", "+79998883221", "Друг"),
                        ("7", "4", "Ivan", "+395672383713", "Friend"),
                        ("8", "4", "John", "+7abcdef", "desc"),
                        ("0", "4", "", "", ""),
                        ("400", "4", "", "", "")])
def test_edit_contact(mocker, index, n, name, number, description):
    """Тестирование изменение контакта"""
    book = ContactBook()
    book.open()
    assert type(book.contacts) == list
    mocker_input = mocker.patch('builtins.input', side_effect=[index, n, name, number, description])
    result = book.edit()
    assert mocker_input.call_count >= 1 and mocker_input.call_count <= 5
    if result is True:
        assert book.contacts[int(index)].name == name
        assert book.contacts[int(index)].number == number
        assert book.contacts[int(index)].description == description

@pytest.mark.parametrize("id", ['0','5','10','15','-100','b', ''])
def test_del_contact(mocker, id):
    """Тестирование удаление контакта"""
    book = ContactBook()
    book.open()
    assert type(book.contacts) == list
    lenght = len(book.contacts)
    mocker_input = mocker.patch('builtins.input', return_value=id)
    result = book.delete()
    assert mocker_input.call_count == 1
    if result:
        assert len(book.contacts) == lenght - 1
    else:
        assert len(book.contacts) == lenght

def test_open_save_file(capsys):
    """Тестирование открытия и сохранения файла"""
    book = ContactBook()
    book.open()
    assert "Файл открыт" in capsys.readouterr().out
    assert type(book.contacts) == list
    book.save()
    assert "Файл сохранен" in capsys.readouterr().out