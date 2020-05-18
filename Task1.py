polish_list = input('Введите выражение ').split()


def polish_notation(oper, num_1, num_2):
    assert oper in ['+', '-', '/', '*'], 'Неизвестный оператор'
    try:
        int(num_1) + int(num_2)
    except ValueError:
        return 'Арифметические операции со строками невозомжны'
    else:
        if oper == '+':
            return int(num_1) + int(num_2)
        elif oper == '-':
            return int(num_1) - int(num_2)
        elif oper == '*':
            return int(num_1) * int(num_2)
        elif oper == '/':
            try:
                int(num_1) / int(num_2)
            except ZeroDivisionError:
                return 'Делить на ноль нельзя'
            else:
                return int(num_1) / int(num_2)


try:
    polish_notation(*polish_list)
except TypeError:
    print('Недостаточно данных')
else:
    print(polish_notation(*polish_list))
