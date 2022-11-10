from random import randint

print('CaNdY GaMe')


def hi_gamer():
    player_name = input('enter ur name:\n')
    bot = 'bot'
    return [player_name, bot]


def get_rules(gamers):
    total_sweets = 2021
    step = 28
    first = int(input(
        f'{gamers[0]} press 1 if u wanna go 1st or other digit if dont\n'))
    if first != 1:
        first = 0
    return [total_sweets, step, int(first)]


def play_game(rules, gamers):
    count = rules[2]
    print(count)
    while rules[0] > 0:
        if not count % 2:
            turn = rules[0] % rules[1]
            print(f'bot takes {turn}')
        else:
            print(f'{gamers[0]}, go on: ')
            turn = int(input())
            if turn > rules[0] or turn > rules[1]:
                print(
                    f'to much, try from 1 to 28')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= turn <= rules[1]:
                        break
                    print(f'try again {attempt} attempts left')
                    turn = int(input())
                    attempt -= 1
                else:
                    return print(f'game over, press Shit+F6')
        rules[0] = rules[0] - turn
        if rules[0] > 0:
            print(f'{rules[0]} sweets left')
        else:
            print('gg')
        count += 1
    return gamers[count % 2]


gamers = hi_gamer()
rules = get_rules(gamers)

winer = play_game(rules, gamers)
print(f'{winer} took all sweets')
