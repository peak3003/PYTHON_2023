# 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while задачки)

n = int(input("Input n: "))
fact = 1
while n >= 0:
    fact *= n
    n -= 1
    if n == 0:
        print(fact)
        break
else:
    print(1)
