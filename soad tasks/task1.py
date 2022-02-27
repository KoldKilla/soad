import random

def m_create():
    try:
        m = int(input('Введите длину матрицы: '))
        if 3 <= m <= 10**3:
            m = m
    except ValueError:
        m = 3

    try:
        max_lim = int(input('Введите максимальное значение генерируемого числа, оно должно быть больше минимального: '))
        if 1 <= max_lim <= 10**6:
            max_lim = max_lim
    except ValueError:
        max_lim = 4


    try:
        min_lim = int(input('Введите минимальное значение генерируемого числа: '))
        if 1 <= min_lim <= 10**6:
            min_lim = min_lim
    except ValueError:
        min_lim = 3


    matrix = [random.randint(min_lim, max_lim) for j in range(m)]
    return matrix

matrix = m_create()
print("Исходные данные:", matrix)

def f_Per(matrix): # Первый номер
    matrix.sort()
    for i in range(len(matrix) - 3, -1, -1):
        if matrix[i] + matrix[i + 1] > matrix[i + 2]:
            a = matrix[i]
            b = matrix[i + 1]
            c = matrix[i + 2]
            print("Для сторон:", a,b,c)
            return matrix[i] + matrix[i + 1] + matrix[i + 2]
    return(0)

print("Максимальный периметр: ", f_Per(matrix))
