def state_of_field():
    print((f'{'-------------'}\n'
           f'| {field[0]} | {field[1]} | {field[2]} |\n'
           f'{'-------------'}\n'
           f'| {field[3]} | {field[4]} | {field[5]} |\n'
           f'{'-------------'}\n'
           f'| {field[6]} | {field[7]} | {field[8]} |\n'
           f'{'-------------'}\n'))

def state_of_play():
    if field[0] == field[1] == field[2]:
        return print('Победа.')
    elif field[3] == field[4] == field[5]:
        return print('Победа.')
    elif field[6] == field[7] == field[8]:
        return print('Победа.')
    elif field[0] == field[3] == field[6]:
        return print('Победа.')
    elif field[1] == field[4] == field[7]:
        return print('Победа.')
    elif field[2] == field[5] == field[8]:
        return print('Победа.')
    elif field[0] == field[4] == field[8]:
        return print('Победа.')
    elif field[2] == field[4] == field[6]:
        return print('Победа.')
    else:
        return print('Ничья.')

player1 = input('Игрок 1, выберите X или O:')
player2 = None
X = 'X'
O = 'O'
if player1 == X:
    player2 = O
elif player1 == O:
    player2 = X
else: print('ОШИБКА: Введён неверный символ.')

field = list(range(1, 10))
state_of_field()
if player1 == X:
    for move in range(1, 8):
        move_player1 = int(input('Игрок 1, куда поставим X ?:'))
        field[move_player1 - 1] = X
        state_of_field()
        state_of_play()

        move_player2 = int(input('Игрок 2, куда поставим O ?:'))
        field[move_player2 - 1] = O
        state_of_field()
        state_of_play()

elif player1 == O:
    for move in range(1, 8):
        move_player1 = int(input('Игрок 1, куда поставим O ?:'))
        field[move_player1 - 1] = O
        state_of_field()
        state_of_play()

        move_player2 = int(input('Игрок 2, куда поставим X ?:'))
        field[move_player2 - 1] = X
        state_of_field()
        state_of_play()
else:
    print('ОШИБКА: Введен неверный символ.')