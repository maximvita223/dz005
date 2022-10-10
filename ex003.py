# Создайте программу для игры в ""Крестики-нолики"".


board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def draw_board(board):
    print(f'_{board[0]}_||_{board[1]}_||_{board[2]}_')
    print(f'_{board[3]}_||_{board[4]}_||_{board[5]}_')
    print(f' {board[6]} || {board[7]} || {board[8]} ')


def check_win(board):
    win_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_combo:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        return False


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f'Куда поставим {player_token}?')
        try:
            player_answer = int(player_answer)
        except:
            print('Вы ввели не корректное значение')
            continue
        if player_answer >= 0 and player_answer <= 8:
            if (str(board[player_answer]) not in 'XO'):
                board[player_answer] = player_token
                valid = True
            else:
                print('Эта клетка уже занята')
        else:
            print('Некорректный ввод')


def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def game(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
game(board)