base = {'Земля': 150, 'Казна': 10000, 'Зерно': 10500, 'Народ': 100, 'Смута': 0, 'Год': 0}

from random import *
someone = 'Кто-то хочет купить зерно по'
bush = 'золотых за бушель. Сколько зерна продать?'
to_people = 'Сколько зерна отдаём народу?'

'''Продаем зерно'''
def sale():
    price = randint (20, 30)
    print ('{} {} {}'.format(someone, price, bush))
    number = (input())
    while True:
        try:
            number = int(number)
            if 0 <= number <= base['Зерно']:
                base['Зерно'] -= int(number)
                base['Казна'] += int(number * price)
                break
            else:
                number = input('Введите корректное число:')

        except KeyError:
            number = input('Введите корректное число:')

        except ValueError:
            number = input('Введите корректное число:')
    print_base()

def print_base():
    for key in base.keys():
        print(key, end ='  ')
    print()
    for value in base.values():
        print(value, end='    ')

    print()

'''Кормим народ'''
def eat():
    change = randint(5,15)
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
                grain_to_people = input('Введите корректное число:')


        except ValueError:
            grain_to_people = input('Введите корректное число:')

        except KeyError:
            grain_to_people = input('Введите корректное число:')



def main():
    while base['Смута']<50 and base['Зерно']>0 and base['Народ']>0:
        print_base()
        sale()
        eat()
        base['Год']+=1
    if base['Смута']>=50:
        print('Вы проиграли, слишком много недовольных Вашим правлением')

    elif base['Зерно']<=0:
        print('Вы проиграли, у вас больше не осталось зерна.')


    elif base['Народ']<= 0:
        print('Вы проиграли, Вы убили весь народ.')

main()
