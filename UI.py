# Интерфейс
import initial
book = initial.get_book()

def hello_user():
    import_data = input(f'Select action:\n Add = 1, delete = 2 , find = 3, break = 4 \n')
    return import_data

def add_name():
    add_name = input(f' Add  name: ')
    return add_name

def add_phone():
    add_phone = input(f'Add phone: ')
    return add_phone

def delete_contact():
    delete_name = input(f'Name to remove: ')
    print(f'Remove succsessfuly: {delete_name}')
    return delete_name
 
def find_contact():
    find_name = input('Name to find: ')
    print(f'Name you are looking for: {find_name}')
    return find_name

