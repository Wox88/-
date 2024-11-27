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
        print('Победа.')
        return True
    elif field[3] == field[4] == field[5]:
        print('Победа.')
        return True
    elif field[6] == field[7] == field[8]:
        print('Победа.')
        return True
    elif field[0] == field[3] == field[6]:
        print('Победа.')
        return True
    elif field[1] == field[4] == field[7]:
        print('Победа.')
        return True
    elif field[2] == field[5] == field[8]:
        print('Победа.')
        return True
    elif field[0] == field[4] == field[8]:
        print('Побада.')
        return True
    elif field[2] == field[4] == field[6]:
        print('Победа.')
        return True
    else:
        return False

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
for move_player1 in range(1, 10):
    if player1 == X:
        move_player1 = int(input('Игрок 1, куда поставим X ?:'))
        field[move_player1 - 1] = X
        state_of_field()
        if state_of_play():
            break

        move_player2 = int(input('Игрок 2, куда поставим O ?:'))
        field[move_player2 - 1] = O
        state_of_field()
        if state_of_play():
            break

    elif player1 == O:
        move_player1 = int(input('Игрок 1, куда поставим O ?:'))
        field[move_player1 - 1] = O
        state_of_field()
        if state_of_play():
            break

        move_player2 = int(input('Игрок 2, куда поставим X ?:'))
        field[move_player2 - 1] = X
        state_of_field()
        if state_of_play():
            break
    else:
        print('ОШИБКА: Введен неверный символ.')
