# Оперрации добавление,удаление, поиск
import csv

import UI

import initial


def add_data():
    book = initial.get_book()
    name = UI.add_name()
    phone = UI.add_phone()
    book[name]=phone
    initial.init_book(book)
    print(book)
    # return book,name,phone


def remote_data():
    name = UI.delete_contact()
    book = initial.get_book()
    del book[name]
    print(book)
    initial.init_book(book)

def find_data():
    name= UI.find_contact()
    book = initial.get_book()
    # for i in book:
    #     if i == name:
    #         print(book[name])
    user_contact = name+ ':' + book[name]
    print(user_contact)