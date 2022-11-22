from pb_model import new_contact
from pb_logic import reading, saving_column, saving_new_line


def menu():
    print('Choose menu item\n'
          '1. New contact\n'
          '2. Show all saved contacts')
    item = int(input())
    if item == 1:
        new = new_contact()
        saving_column(new)
        saving_new_line(new)
    elif item == 2:
        print(reading())
    else:
        print('choose one of menu items')

