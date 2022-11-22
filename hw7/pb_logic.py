from pb_model import new_contact as cont


def saving_new_line(cont):
    pb = 'PB.csv'
    with open(pb, 'a') as add:
        add.write(f'last name: {cont[0]}; first_name: {cont[1]}; phone number: {cont[2]}; description: {cont[3]}\n')


def saving_column(cont):
    pb = 'PB_line.csv'
    with open(pb, 'a') as add:
        add.write(f'last name: {cont[0]}\nfirst_name: {cont[1]}\nphone number: {cont[2]}\ndescription: {cont[3]}\n\n')


def reading():
    with open('PB.csv', 'r') as r:
        return r.read()
