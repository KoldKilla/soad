#!/usr/bin/env python
# coding: utf-8

# # Лабораторная работа №2
# ## Выполнил студент группы БСТ2002 Демидов Константин 
# ### Задание №1

# #### Реализовать методы поиска в соответствии с заданием. Организовать генерацию начального набора случайных данных. Для всех вариантов добавить реализацию добавления, поиска и удаления элементов. Оценить время работы каждого алгоритма поиска и сравнить его со временем работы стандартной функции поиска, используемой в выбранном языке программирования.

# ### Подключение библиотек

# In[6]:


from IPython.display import HTML, display
import random
import time
from random import randint
import copy


# In[9]:


def Print(mas, n):
    for i in range (int(n)):
        print(mas[i], end=' ')
    print()
    
n = int(input("Введите количество элементов : "))
min_limit = input("Укажите начальный диапозон чисел для генерации: ")
max_limit = input("Укажите конечный диапозон чисел для генерации: ")
mas = [randint(int(min_limit), int(max_limit)) for i in range(int(n))]


mas.sort()
print("Сгенерированные элементы: ")
Print(mas, n)

def Insert(mas):
    print("Хотите внести элемент? ")
    ans = input()
    if ans=="да" :
        el = int(input("Введите число: "))
        index = int(input("Введите индекс: "))
        mas.insert(index, el)
        Print(mas, n + 1)

def Delete(mas):
    print("Хотите удалить элемент? ")
    ans = input()
    if ans == "да" :
        index = int(input("Введите индекс: "))
        del mas[index]
        Print(mas, n - 1)


# ### Бинарный поиск

# In[10]:


def BinSearch(arr, x):
    m = len(arr) // 2
    i = 0
    j = len(arr)-1
    while arr[m] != x and i<= j:
        if x > arr[m]:
            i = m + 1
        else:
            j = m - 1
        m = (i + j) // 2
    if i > j:
        print("Искомого числа в массиве нет")
    else:
        print("Индекс: ", m)


# In[11]:


print("Бинарный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_bin = copy.deepcopy(mas)
start = time.time()
BinSearch(mas_bin, element)
end = time.time()-start
print("Время затраченное на поиск: ",'%.16f' % end)
Insert(mas_bin)
Delete(mas_bin)


# ### Бинарное дерево

# In[12]:


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                print(lkpval, "не найден.")
                return False
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                print(lkpval, "не найден.")
                return False
            return self.right.findval(lkpval)
        else:
            print(self.data, ' найден.')
            return True

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


def make_a_tree(arr):
    root = Node(arr[0])
    for i in arr[1::]:
        root.insert(i)
    return root


# In[14]:


print("Бинарное деререво")
mas_tree = copy.deepcopy(mas)
root = make_a_tree(mas_tree)
num = int(input("Введите элемент, который хотите найти: "))
start = time.time()
result = root.findval(num)
end= time.time() - start
print("Время затраченное на поиск: ", end)
task = input("Хотите внести элемент? ")
if task == "да" :
    num = int(input("Введите элемент, который хотите внести: "))
    root.insert(num)
    root.PrintTree()
task = input("Хотите удалить элемент? ")
if task == "да" :
    num = int(input("Введите элемент, который хотите удалить: "))
    mas_tree.remove(num)
    root = make_a_tree(mas_tree)
    root.PrintTree()


# ### Фибоначев поиск

# In[15]:


def FibonacciSearch(lys, val):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while (fibM < len(lys)):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(lys)-1))
        if (lys[i] < val):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (lys[i] > val):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else :
            return i
    if(fibM_minus_1 and index < (len(lys)-1) and lys[index+1] == val):
        return index+1
    return -1


# In[34]:


print("Фибоначчиев поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_fib = copy.deepcopy(mas)
start = time.time()
a = FibonacciSearch(mas_fib,element)
end = time.time()-start
if a == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", a)
print("Время затраченное на поиск: ", end)
Insert(mas_fib)
Delete(mas_fib)


# ### Интерполяционный

# In[20]:


def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / (lys[high] - lys[low])) * (val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1
        else:
            high = index - 1
    return -1


# In[46]:


#интерполяционный поиск
print("Интерполяционный поиск")
print("Введите элемент, который хотите найти: ")
element = int(input())
mas_inter = copy.deepcopy(mas)
start_time_inter = time.time()
b = InterpolationSearch(mas_inter, element)
end_time_inter = time.time()-start_time_inter
if b == -1:
    print("Искомого числа в массиве нет")
else:
    print("Индекс: ", b)
print("Время работы: ", end_time_inter)
Insert(mas_inter)
Delete(mas_inter)


# ### Задание №2

# ### Простое рехеширование

# In[22]:


def generate_array(length=100):  # генерируем случайный массив
    array = []
    while len(array) < length:
        array.append(random.randint(0, 100))
    return array
class ClassForRehash:
    """
    Класс для наглядных примеров рехэширования с крайне примитивным хэшированием (для наглядности). \r\n
        Особенность:
            -Хеш зависит только от единиц в числе value1 (для удобства создания коллизий)
    """
    def __init__(self, value1):
        self.value1 = value1
        self.hash = int((((value1 % ClassForRehash.MAX_HASH_TABLE) * 331) & 127) % ClassForRehash.MAX_HASH_TABLE)

    MAX_HASH_TABLE = 8


# In[23]:


class SimpleRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = element
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, element.hash))
            return

        """""
        простое рехеширование
        """""
        new_hash = original_hash + 1
        while new_hash != original_hash:
            if new_hash >= len(self.table):
                new_hash = 0
                continue
            if self.table[new_hash] is None:
                element.hash = new_hash
                self.table[new_hash] = element
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                return
            new_hash += 1
        print("таблица заполнена!")
        return


# In[24]:


class SimpleRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = element
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, element.hash))
            return

        new_hash = original_hash + 1
        while new_hash != original_hash:
            if new_hash >= len(self.table):
                new_hash = 0
                continue
            if self.table[new_hash] is None:
                element.hash = new_hash
                self.table[new_hash] = element
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                return
            new_hash += 1
        print("таблица заполнена!")
        return


# In[25]:


simple_re = SimpleRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(simple_re.table) + 2):
    simple_re.add_el(ClassForRehash(random.randint(0, 9)))


# ### Случайное рехеширование

# In[26]:


class RandomRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = element
            print("объект со значением %i имеет хэш: %i (рехеширование не требовалось)"
                  % (self.table[original_hash].value1, original_hash))
            return

        table_len = len(self.table)
        r = 1
        for ii in range(10):  # range(число попыток определить новый хеш)
            r *= 5
            r = r % (4 * table_len)
            new_hash = r // 4
            if self.table[new_hash] is None:
                element.hash = new_hash
                self.table[new_hash] = element
                print("объект со значением %i имеет хэш: %i (рехешировано. коллизия была в хеше: %i)"
                      % (self.table[new_hash].value1, element.hash, original_hash))
                return
        print("Не удалось найти свободный хеш в таблице!")
        return


# In[27]:


random_re = RandomRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(random_re.table) + 2):
    random_re.add_el(ClassForRehash(random.randint(0, 9)))


# ### Метод цепочек

# In[28]:


class ChainRehashTable:

    def __init__(self, length):
        self.table = [None] * length

    def add_el(self, element):
        """""
        метод цепочек
        """""
        original_hash = element.hash
        if self.table[original_hash] is None:
            self.table[original_hash] = [element]
            return
        else:
            length = len(self.table[original_hash])
            self.table[original_hash].append(element)
            return


# In[48]:


chain_re = ChainRehashTable(ClassForRehash.MAX_HASH_TABLE)
for i in range(len(chain_re.table) + 2):
    chain_re.add_el(ClassForRehash(random.randint(0, 9)))
hash = 0
for x in chain_re.table:  # вывод хеш таблицы для метода цепочек
    print("[hash: %i]" % hash, end=" ")
    if x is None:
        print("Empty")
    else:
        for y in x:
            print(y.value1, end=" ")
        print("")
    hash += 1


# ### Задание №3

# #### Расставить на стандартной 64-клеточной шахматной доске 8 ферзей так, чтобы ни один из них не находился под боем другого». Подразумевается, что ферзь бьёт все клетки, расположенные по вертикалям, горизонталям и обеим диагоналямНаписать программу, которая находит хотя бы один способ решения задач.

# In[30]:


def make_quins_attack(array):
    """
    пересчитывает клетки под атакой на всём поле
    """
    length = len(array)
    for y in range(length):  # очищаем закрытые клетки
        for x in range(length):
            if array[y][x] == 1:
                array[y][x] = 0
    for y in range(length):  # закрываем клетки
        for x in range(length):
            if array[y][x] == 2:
                buffer = 0
                for i in range(length):
                    if array[i][x] == 0:  # закрываем клетки по вертикали
                        array[i][x] = 1
                    if array[y][i] == 0:  # закрываем клетки по горизонтали
                        array[y][i] = 1
                    # закрываем клетки по диагонали \
                    if x >= y and length > x - y + i >= 0:  # королева в верхней правой части доски
                        if array[i][x - y + i] == 0:
                            array[i][x - y + i] = 1
                    elif length > y - x + i >= 0:  # королева в нижней левой части доски
                        if array[y - x + i][i] == 0:
                            array[y - x + i][i] = 1
                    # закрываем клетки по диагонали /
                    if x + y <= length and length > x + y - i >= 0:  # королева в верхней левой части доски
                        if array[i][x + y - i] == 0:
                            array[i][x + y - i] = 1
                    elif length > y + x - i >= 0:  # королева в нижней правой части доски
                        if array[y + x - i][i] == 0:
                            array[y + x - i][i] = 1


def filling_quins(array, quins_amount):
    length = len(array)
    for y in range(length):
        for x in range(length):
            if array[y][x] == 0:  # нашли свободное место для королевы
                array[y][x] = 2
                quins_amount -= 1
                make_quins_attack(array)
                if quins_amount == 0:  # королев не осталось
                    return 1  # королевы успешно расставленны
                if filling_quins(array, quins_amount) == 1:
                    return 1  # королевы успешно расставленны
                else:
                    array[y][x] = 0
                    quins_amount += 1
                    make_quins_attack(array)
    return -1  # неудача


def chess_2(board_length, quins_amount):
    board = [0] * board_length
    for i in range(board_length):  # формируем нашу доску как массив из массивов
        board[i] = [0] * board_length
    if filling_quins(board, quins_amount) == 1:  # ищем доску
        print("Комбинация найдена!")
    else:
        print("Комбинации не существует!")
    return board


# In[32]:


class Colors:
    WHITE = '\u001b[47m'
    BLACK = '\u001b[48m'
    RESET = '\u001b[0m'
    

our_board = chess_2(8, 8)

white_f = False
for y in our_board:
    for x in y:
        if white_f:
            white_f = False
        else:
            white_f = True
        if x == 0:
            if white_f:
                print(Colors.WHITE + " O " + Colors.RESET, end='')
            else:
                print(Colors.BLACK + " O " + Colors.RESET, end='')
        elif x == 1:
            print(Colors.WHITE + " C " + Colors.RESET, end='')
        else:
            print(Colors.BLACK + " Q " + Colors.RESET, end='')
    print('')
    if white_f:
        white_f = False
    else:
        white_f = True

