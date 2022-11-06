import Model
import View

def start():
    open_file()
    View.printPhoneBook()
    View.main_menu()
    choice_function()


def choice_function():
    while True:
        choice = int(input('Выберите пункт: '))
        if choice == 0:
            break
        if choice == 1:
            open_file()
            View.printPhoneBook()
        if choice == 2:
            save_file()
            print('\nФайл с контактами сохранен!\n')
        if choice == 3:
            add_contact()
            print('\nКонтакт добавлен\n')
        if choice == 4:
            change_contact()
        if choice == 5:
            remove_contact()
            print('\nКонтакт удален\n')
        if choice == 6:
            search_contact()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()

def search_contact():
    text = input('Введите слово для поиска контакта: ')
    found = False
    for item in Model.phonebook:
        if item.__contains__(text):
            print(item)
            found = True
    if not found: print('Ничего не найдено')