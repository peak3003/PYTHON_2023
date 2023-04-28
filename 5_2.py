# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

#Без рекурсии:

import random

def replacement (some_list):
    min_item = min(some_list)
    max_item = max(some_list)
    for i in range(len(some_list)):
        if some_list[i] == max_item:
            some_list[i] = min_item
    return some_list

some_list = [random.randint(1, 6) for _ in range(5)]

print(some_list)
print(replacement(some_list))


def lst_print(n, lst, k=0):
    if k == 0:
        print(1 if lst[0] > 3 else lst[0], end=' ')
    if k == n - 1:
        print(1 if lst[n - 1] >= 3 else lst[n - 1], end=' ')
        return lst[n - 1]
    else:
        print(1 if lst[k + 1] > 3 else lst[k + 1], end=' ')
        return lst_print(n, lst, k + 1)


lst_print(5, [1, 3, 4, 3, 3, 4])

