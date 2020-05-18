# Добавлена функция def show_name, строки 81-91
# Расширена функция def comands, строки 103, 114-115

documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

directories = {
  '1': ['2207 876234', '11-2', '5455 028765'],
  '2': ['10006'],
  '3': []
}


def people():
    """
    Спрашивает номер документа и выводит имя человека, которому он принадлежит
    """
    document = input('Введите номер документа ')
    for document_number in documents:
        if document_number.get('number') == document:
            print(document_number.get('name'))
        break
    else:
        print('Такого человека нет в базе данных')


def shelf():
    """
    Спрашивает номер документа и выводит номер полки, на которой он находится
    """
    document = input('Введите номер документа ')
    for shelf_number, document_number in directories.items():
        for number in document_number:
            if number == document:
                 print(f'Документ находится на полке №{shelf_number}')
                 break
    else:
        print('Такого документа нет в базе данных')


def lists():
    """
    Выводит список всех документов
    """
    for the_document in documents:
        print(f"'{the_document.get('type')}' '{the_document.get('number')}' '{the_document.get('name')}'")


def add():
    """
    Добавляет новый документ в каталог и полку
    """
    doc_shelf = input('Введите номер полки, на которой будет храниться документ ')
    doc_number = input('Введите номер документа ')
    doc_type = input('Введите тип документа ')
    doc_name = input('Введите имя владельца документа ')
    new_dict = {'type': doc_number, 'number': doc_type, 'name':   doc_name}
    if doc_shelf in directories.keys():
        documents.append(new_dict)
        directories[doc_shelf].append(doc_number)
        print('Данные успешно добавлены')
    else:
        print('Такой полки не существует')


def add_shelf():
    """
    Создаёт новую полку
    """
    new_shelf = input('Введите номер новой полки ')
    if new_shelf in directories.keys():
        print('Такая полка уже существует')
    else:
        directories[new_shelf] = []
        directories.update()
        print(f'Полка №{new_shelf} создана')


def show_name():                                     # Новая функция
    """
    Отображает имена всех владельцев документов
    """
    for the_document in documents:
        try:
            the_document['name']
        except KeyError:
            print(f'У документа {the_document["number"]} отсутствует владелец')
        else:
            print(f'{the_document.get("name")}')


def comands():
    """
    Список всех команд
    """
    while True:
        user_input = input('Выберите команду:\n P - узнать имя человека по номеру документа\n '
                           'S - узнать номер полки, где расположен документ\n L - список всех документов\n '
                           'A - добавить новый документ\n AS - добавить новую полку\n '
                           'SN - показать имена всех владельцев документов, Q - выход из программы\n')
        if user_input == 'P':
            people()
        elif user_input == 'S':
            shelf()
        elif user_input == 'L':
            lists()
        elif user_input == 'A':
            add()
        elif user_input == 'AS':
            add_shelf()
        elif user_input == 'SN':                     # Запуск новой функции
            show_name()
        elif user_input == 'Q':
            break
        else:
            print('Такой команды не существует')
            break


comands()
