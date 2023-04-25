# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
print("Введите элементы элементы первого множества:")
a = [int(input()) for I in range(0, n)]
print("Массив: ", a)
print("Введите элементы элементы второго множества:")
b = [int(input()) for I in range(0, m)]
print("Массив: ", b)
c = list(set(a) & set(b))
c.sort()
print("Числа, которые повторяются: ",c)