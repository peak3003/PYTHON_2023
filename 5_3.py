# Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать
# это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны.
# Примеры:
# [1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
# [1,4,3,2] => "1-4"
# [1,4] => "1,4"

some_list = [1, 2, 4, 3, 9, 8, 11, 0, 13]
some_list.sort()
result_list = []
temp_list = []
print(some_list)
for i in range(0, len(some_list) - 1):
    if some_list[i + 1] - some_list[i] == 1:
        temp_list.append(some_list[i])
    else:
        temp_list.append(some_list[i])
        result_list.append(temp_list)
        temp_list = []
if temp_list:
    result_list.append(temp_list)

if some_list[-1] - some_list[-2] == 1:
    result_list[-1].append(some_list[-1])
else:
    result_list.append([some_list[-1]])

print_list = []
for i in result_list:
    if len(i) > 1:
        print_list.append(f'{i[0]}-{i[-1]}')
    else:
        print_list.append(i[0])
print(*print_list, sep=',')
