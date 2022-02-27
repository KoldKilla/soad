import random

def m_create():
    try:
        m = int(input('Введите количество столбцов в матрице: '))
        if 1 <= m <= 100:
            m = m
    except ValueError:
        m = 1

    try:
        n = int(input('Введите количество строк в матрице: '))
        if 1 <= n <= 100:
            n = n
    except ValueError:
        n = 1

    try:
        min_lim = int(input('Введите минимальное значение генерируемого числа: '))
        if 1 <= min_lim <= 100:
            min_lim = min_lim
    except ValueError:
        min_lim = 1

    try:
        max_lim = int(input('Введите максимальное значение генерируемого числа, оно должно быть больше минимального: '))
        if 1 <= max_lim <= 100:
            max_lim = max_lim
    except ValueError:
        max_lim = 2

    matrix = [[random.randint(min_lim, max_lim) for j in range(m)] for i in range(n)]
    return matrix

matrix = m_create()
print("Исходные данные:", matrix)

def sort(matrix): # Третий номер
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        a = [matrix[i + j][j] for j in range(min(m - i, n))]
        a.sort()
        for j in range(min(m - i, n)):
            matrix[i + j][j] = a[j]
    for j in range(1, n):
        a = [matrix[i][j + i] for i in range(min(n - j, m))]
        a.sort()
        for i in range(min(n - j, m)):
            matrix[i][j + i] = a[i]
    return matrix

print("\nОтсортированная матрица: ", sort(matrix))