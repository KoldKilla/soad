#У вас есть a монет стоимостью n и b монет стоимостью 1. Вы всегда платите без сдачи,
# поэтому вам хочется узнать, существуют ли такие x и y, что если вы возьмете x (0≤x≤a)
# монет стоимостью n и y (0≤y≤b) монет стоимостью 1, суммарная стоимость всех выбранных монет составит S.
# Вам необходимо ответить на q независимых наборов входных данных.
# Стоимость: 1000 (https://codeforces.com/contest/1256/problem/A)

t = int(input()) # Количество данных
for i in range(t):
    a, b, n, s = list(map(int, input().split())) # Ввод набора данных
    if s % n <= b and a * n + b >= s:
        print("Yes")
    else:
        print("No")