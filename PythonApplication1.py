import os

def print_data():
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        phonebook_str = file.read()
        print(phonebook_str)
        
def input_name():
    return input('Input the name: ').title()

def input_surname():
    return input('Input the surname: ').title()

def input_patronymic():
    return input('Input the patronymic: ').title()

def input_phone():
    return input('Input the phone number: ').title()

def input_address():
    return input('Input the address: ').title()

def input_data():
    name = input_name()
    surname = input_surname()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{name} {surname} {patronymic} {phone}\n{address}\n\n'

def add_contact():
    contact_str = input_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        file.write(contact_str)
        
def search_contact():
    search = input('Input data to be searched: ').title()
    print()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_list = file.read().rstrip().split('\n\n')
    for contact_str in contact_list:
        if search in contact_str:
            print(contact_str)
            return
    print('No contact found')
    return

def copy_contact():
    str_num = int(input('Input the string number: ')) - 1
    print()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contact_list = file.read().rstrip().split('\n\n')
    with open('phonebookCopy.txt', 'a', encoding='utf-8') as file:
        file.write(contact_list[str_num])

def interface():
    with open('phonebook.txt', 'a', encoding='utf-8'):
        pass
    command = ''
    print('Menu:\n'
        '1. Print data\n'
        '2. Add contact\n'
        '3. Search for a contact\n'
        '4. Copy a contact\n'
        '5. Exit\n')
    command = input('Input selection: ')
    
    while command not in ('1', '2', '3', '4', '5'):
        print('Invalid selection. Repeat your selection')
        command = input('Input selection: ')

    match command:
        case '1':
            print_data()
        case '2':
            add_contact()
        case '3':
            search_contact()
        case '4':
            copy_contact()
        case '5':
            print('Goodbye')
        
if __name__ == '__main__':
    interface()
