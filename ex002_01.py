#  Добавьте игру против бота
from random import randint, random


candy = 2021
turn = 0
while candy >= 28:
    if turn % 2 == 0:
        while True:
            gamer = input('Введите сколько конфет хотите взять - ')
            try:
                gamer = int(gamer)
                break
            except:
                if gamer.isalpha():
                    print("Введены буквы")
                else:
                    print("Введены непонятные символа")
    else:
        bot=randint(1,28)
        candy-=bot
        print(f'Бот взял {bot} Осталось конфет {candy}')
    if gamer > 0 and gamer <= 28:
        candy -= gamer
        turn += 1
        print(f' Осталось {candy}')
    else:
        print('Введено неправильное количество конфет')
while candy != 0:
    if turn%2==0:
        gamer = int(input('Введите сколько конфет хотите взять - '))
        if gamer > candy:
            print('Вы не можете взять больше чем есть')
        else:
            candy -= gamer
            turn += 1
            print(f'Осталось {candy}')
    else:
        print(f'Бот взял {candy}')
        candy-=candy
        turn+=1
        print(f'Осталось конфет {candy}')        


if turn % 2 == 0:
    print('Победил бот ')
else:
    print('Победил Игрок')
