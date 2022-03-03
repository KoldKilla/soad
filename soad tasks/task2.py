import random

def m_create():
    try:
        m = int(input('Введите длину матрицы: '))
        if 1 <= m <= 100:
            m = m
    except ValueError:
        m = 1

    try:
        max_lim = int(input('Введите максимальное значение генерируемого числа, оно должно быть больше минимального: '))
        if 0 <= max_lim <= 10**9:
            max_lim = max_lim
    except ValueError:
        max_lim = 1

    try:
        min_lim = int(input('Введите минимальное значение генерируемого числа: '))
        if 0 <= min_lim <= 10**9:
            min_lim = min_lim
    except ValueError:
        min_lim = 0


    matrix = [random.randint(min_lim, max_lim) for j in range(m)]
    return matrix

matrix = m_create()
print("Исходные данные:", matrix)

def max_number(matrix): # Второй номер
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            firstNumber = str(matrix[i]) + str(matrix[j])
            secondNumber = str(matrix[j]) + str(matrix[i])
            if firstNumber < secondNumber:
                matrix[i], matrix[j] = matrix[j], matrix[i]
    result = ""
    for i in matrix:
        result += str(i)
    return str(int(result))

print("Получившееся число: ", max_number(matrix))