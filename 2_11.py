# 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# вариант1
a = int(input("Input A: "))
fib = [0, 1]
while fib[len(fib) - 1] < a:
    fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
if a != fib[len(fib) - 1]:
    print(-1)
else:
    print(len(fib))

# вариант2
a = int(input("Input A: "))
fiba = 0
fibb = 1
count = 2
while fibb < a:
    fibc = fiba + fibb
    fiba = fibb
    fibb = fibc
    count += 1
if a != fibb:
    print(-1)
else:
    print(count)
