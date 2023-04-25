# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка# содержит число X

# мое решение
n = int(input("Введите количество элементов: "))
print("Введите элементы массива:")
a = [int(input()) for I in range(0, n)]
print("Массив: ", a)
x = int(input("Введите число Х "))
print("Самый близкий по величине элемент к заданному Х: ", min(a, key=lambda a: abs(a - x)))

# решение 1

import random

rnd_list = [random.randint(-100, 100) for in range(10)]
x = int(input())
print(rnd_list)
min_diff = abs(rnd_list[0] - x)
for el in rnd_list:
    if abs(el - x) < min_diff:
        min_diff = abs(el - x)
        find_el = el
print(find_el)

# решение 2 (проверяем в стороны от нашего элемента +1 -1 и проверяем наличие. Если нет, то смотрим +2 -2 и тд)
import random

rnd_list = [random.randint(-100, 100) for in range(10)]
x = int(input())
print(rnd_list)
some_set = set(rnd_list)
diff = 0
while True:
    if x + diff in some_set:
        print(x + diff)
        break
    elif x - dict in some_set:
        print(x - diff)
        break
    diff += 1
