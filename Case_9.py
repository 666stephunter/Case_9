base = {'Земля': 150, 'Казна': 10000, 'Зерно': 10500, 'Народ': 100, 'Смута': 0, 'Год': 0}

from random import *
from ru_local import *

'''Продаем зерно'''


def sale():
    price = randint(20, 30)
    print('{} {} {}'.format(someone, price, bush))
    number = (input())
    while True:
        try:
            number = int(number)
            if 0 <= number <= base['Зерно']:
                base['Зерно'] -= int(number)
                base['Казна'] += int(number * price)
                break
            else:
                number = input(exception)

        except KeyError:
            number = input(exception)

        except ValueError:
            number = input(exception)
    print_base()


def print_base():
    for key in base.keys():
        print(key, end ='  ')
    print()
    for value in base.values():
        print(value, end='    ')

    print()


'''Засеиваем зерно'''


def seed():
    print(suggestion)
    grain_seed = int(input())
    print(grain_seed)
    while True:
            if 0 < int(grain_seed) <= int(base['Зерно']):
                base['Зерно'] -= int(grain_seed)
                break
            elif int(grain_seed) > base['Зерно']:
                print(lack)
                grain_seed = input()

            elif grain_seed == 0:
                print(next)
                next_step = input()
                if next_step == 'y':
                    break
            else:
                print(exception)
                grain_seed = input()



'''Кормим народ'''


def eat():
    change = randint(5, 15)
    print('{}'.format(to_people))
    grain_to_people = input()
    while True:
        try:
            grain_to_people = int(grain_to_people)
            if 0 <= grain_to_people <= base['Зерно']:
                base['Зерно'] -= int(grain_to_people)
                if grain_to_people < int(base['Народ']*3):
                    base['Народ'] -= int(change)
                    base['Смута'] += int(change)

                else:
                    base['Народ'] += int(change)

                break
            else:
                grain_to_people = input(exception)

        except ValueError:
            grain_to_people = input(exception)

        except KeyError:
            grain_to_people = input(exception)


def main():
    while base['Смута'] < 50 and base['Зерно'] > 0 and base['Народ'] > 0:
        print_base()
        sale()
        seed()
        eat()
        base['Год'] += 1
    if base['Смута'] >= 50:
        print(end1)

    elif base['Зерно'] <= 0:
        print(end2)

    elif base['Народ'] <= 0:
        print(end3)


main()
