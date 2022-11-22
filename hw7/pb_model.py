
def new_contact():
    contact = []
    last_name = input('Enter last name: ')
    contact.append(last_name)
    first_name = input('Enter first name: ')
    contact.append(first_name)
    phone_num = input('Enter phone number: ')
    contact.append(phone_num)
    desc = input('Enter description: ')
    contact.append(desc)

    return contact
