# Создайте программу для игры с конфетами человек против человека.

candy = 2021
turn = 0
while candy >= 28:
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
    if gamer > 0 and gamer <= 28:
        candy -= gamer
        turn += 1
        print(f'Осталось {candy}')
    else:
        print('Введено неправильное количество конфет')
while candy != 0:
    gamer = int(input('Введите сколько конфет хотите взять - '))
    if gamer > candy:
        print('Вы не можете взять больше чем есть')
    else:
        candy -= gamer
        turn += 1
        print(f'Осталось {candy}')


if turn % 2 == 0:
    print('Победил 2 игрок ')
else:
    print('Победил 1 Игрок')
