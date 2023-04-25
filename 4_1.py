# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# some_str = input()
import random

some_str = [chr(random.randint(32, 100)) for _ in range(10)]
# some_str = [chr(random.randint(32, 100)) for _ in (10 ** 3)]

# import time
#
# # ВСТРОЕННЫЙ МЕТОД count
# start = time.perf_counter()
# for letter in set(some_str):
#     a = letter, some_str.count(letter)
# end = time.perf_counter()
# duration1 = end - start
#
# # свой метод
# start = time.perf_counter()
# for letter in set(some_str):
#     amount = 0
#     for letter1 in some_str:
#         if letter == letter1
#             amount += 1
#     a = letter, amount
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration2 / duration1)

# через словари, сложность линейная
print(some_str)
count_dict = {}  # a:3
for letter in some_str:
    if letter not in count_dict:
        count_dict[letter] = 1
    else:
        count_dict[letter] = count_dict[letter] + 1
print(count_dict)
