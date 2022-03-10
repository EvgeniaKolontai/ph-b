
import UI
import controller

def chek_comnad():
    command = 0
    while  command != '5':
        command =UI.hello_user()
        if command == '1':
            controller.add_data()
        elif command == '2':  
            controller.remote_data()
        elif command == '3':
            controller.find_data()
        elif command == '4':
            break
