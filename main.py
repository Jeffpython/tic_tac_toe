import random


def display_info(field: list[list[str | None]], is_field_filled: bool, is_win: bool, move_by='comp') -> None:
    ''' отображать в консоли информацию о состоянии игры '''

    display_field(field)

    if is_field_filled:
        print('Победила - дружба!')
    elif is_win:
        print('Вы проиграли') if move_by == 'comp' else print('Вы выиграли!')


def display_field(field: list[list[str | None]]) -> None:
    ''' отобразить игровое поле '''

    for row in field:
        print('-' * 13)

        for cell in row:
            if cell:
                print(f'| {cell} ', end='')
            else:
                print('|   ', end='')

        print('|')
    print('-' * 13)


def make_move(field: list[list[str | None]], is_user_play_by_crosses: bool, move_by='comp') -> None:
    ''' выполнить ход '''

    while True:

        if move_by == 'user':
            row = int(input('Введите строку": ')) - 1
            column = int(input('Введите столбец": ')) - 1
            is_correct_move = check_move(field, row, column)

            if is_correct_move:
                field[row][column] = 'X' if is_user_play_by_crosses else '0'
                break
            else:
                print('Указано ошибочное поле')
        else:
            row = random.randint(0, 2)
            column = random.randint(0, 2)
            is_correct_move = check_move(field, row, column)

            if is_correct_move:
                field[row][column] = '0' if is_user_play_by_crosses else 'X'
                break


def check_move(field: list[list[str | None]], row: int, column: int) -> bool:
    ''' проверка корректности хода '''

    # вне игрового поля
    if row > 2 or column > 2:
        return False

    # поле заполнено
    if field[row][column]:
        return False

    return True


def check_field_fill(field: list[list[str | None]]) -> bool:
    ''' заполненность игрового поля '''
    for row in field:
        for cell in row:
            if cell is None:
                return False

    return True


def check_rows_same_values(field: list[list[str | None]]) -> bool:
    ''' проверка заполнения строк одинаковыми значениями '''
    if (field[0][0] and field[0][0] == field[0][1] == field[0][2]
            or field[1][0] and field[1][0] == field[1][1] == field[1][2]
            or field[2][0] and field[2][0] == field[2][1] == field[2][2]):
        return True
    else:
        return False


def check_columns_same_values(field: list[list[str | None]]) -> bool:
    ''' проверка заполнения столбцов одинаковыми значениями '''
    if (field[0][0] and field[0][0] == field[1][0] == field[2][0]
            or field[0][1] and field[0][1] == field[1][1] == field[2][1]
            or field[0][2] and field[0][2] == field[1][2] == field[2][2]):
        return True
    else:
        return False


def check_diagonals_same_values(field: list[list[str | None]]) -> bool:
    ''' проверка заполнения диагоналей одинаковыми значениями '''
    if (field[0][0] and field[0][0] == field[1][1] == field[2][2]
            or field[0][2] and field[0][2] == field[1][1] == field[2][0]):
        return True
    else:
        return False


def check_win(field: list[list[str | None]]) -> bool:
    ''' проверка выигрыша '''
    if (check_rows_same_values(field)
            or check_columns_same_values(field)
            or check_diagonals_same_values(field)):
        return True

    return False


def generate_blank_field() -> list[list[str | None]]:
    ''' генерация пустого игрового поля '''
    return [[None] * 3 for i in range(3)]


def main():

    field = generate_blank_field()
    is_field_filled = False  # поле заполнено
    is_win = False  # выявлен победитель
    is_user_play_by_crosses = random.choice([True, False])  # пользователь играет крестиками

    if is_user_play_by_crosses:
        make_move(field, is_user_play_by_crosses, 'user')
        display_info(field, is_field_filled, is_win, 'user')

    while not is_field_filled and not is_win:

        make_move(field, is_user_play_by_crosses)
        is_field_filled = check_field_fill(field)
        is_win = check_win(field)
        display_info(field, is_field_filled, is_win)

        if not is_field_filled and not is_win:
            make_move(field, is_user_play_by_crosses, 'user')
            is_field_filled = check_field_fill(field)
            is_win = check_win(field)
            display_info(field, is_field_filled, is_win, 'user')


if __name__ == '__main__':
    main()
