# На вход программе подается два натуральных числа a и b (a < b).
# Напишите программу, которая находит все простые числа от a до b включительно.


a = int(input("Input A: "))
b = int(input("Input B: "))
eazy = list()
while a < b:
    for i in range(2, 6):
        if a % i == 0:
            break
    else:
        eazy.append(a)
a += 1
print(eazy)

#Мухаммад  кому  Все 21:45

a = int(input("A"))
b = int(input("B"))
for i in range(a, b + 1):
    for j in range(2, i):
        if i % j != 0:
            print(i)


# вар
a, b, = int(input()), int(input())
for i in range(a, b + 1):
    if i == 1:              # 1 не является простым числом
        continue            # пропускаем цикл
    for j in range(2, i):   # перебираем делители от 2 до i
        if i % j == 0:      # если делится без остатка, то оно не простое
            break           # завершаем вложенный цикл
    else:
        print(i)
