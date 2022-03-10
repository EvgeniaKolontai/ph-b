

book ={'abc':'123'}

def init_book(new_book):
    global book
    book = new_book

def get_book():
    global book
    return book