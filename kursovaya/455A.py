# Леша не любит скучать. Поэтому, когда ему скучно, он придумывает игры. Как-то раз Леша придумал следующую игру.
# Задана последовательность a, состоящая из n целых чисел. Игрок может сделать несколько ходов.
# За один ход игрок может выбрать некоторый элемент последовательности (обозначим выбранный элемент ak) и удалить его,
# при этом из последователости также удаляются все элементы, равные ak+1 и ak-1. Описанный ход приносит игроку ak очков.
# Леша максималист и поэтому хочет набрать как можно больше очков. Какое максимальное количество очков он сможет набрать?
# Стоимость: 1500 (https://codeforces.com/problemset/problem/455/A)
# Итого: 1500 + 1500 + 1000 + 1000 = 3000 + 2000 = 5000

int(input())
arr = [0] * 100001

for x in map(int, input().split()):
    arr[x] += x

a = 0
t_max = 0

for i in arr:
    a, t_max = max(a, i + t_max), a # Прибавление позапрошлого числа
print(a)