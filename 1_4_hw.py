# Задача 8: Требуется определить, можно ли от шоколадки размером n× m
# долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print("Введите размер шоколадки: ")
n = int(input("n "))
m = int(input("m "))
k = int(input("Сколько долек хотите отломить: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print("YES")
else:
    print("NO")
