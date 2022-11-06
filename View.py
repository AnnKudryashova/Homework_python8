import Model


def printPhoneBook():
    for i, item in enumerate(Model.phonebook):
        print(i , item)

def main_menu():
        print('\nГлавное меню:')
        print('0. Выход из меню')
        print('1. Показать все контакты')
        print('2. Записать файл с контактами')
        print('3. Добавить контакт')
        print('4. Изменить контакт')
        print('5. Удалить контакт')
        print('6. Поиск по контактам')