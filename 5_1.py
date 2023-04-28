# Последовательностью Фибоначчи называется последовательность чисел a0 , a1 , ..., an
# , ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

def fibonachi(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonachi(n - 1) + fibonachi(n - 2)


number_N = int(input())
print(fibonachi(number_N))

# разбор
import time

def fib(n):
    if n in (0, 1):
        return
    return fib(b - 1) + fib(n - 2)

start = time.perf_counter()
print(fib(6))
end = time.perf_counter()
duration1 = end - start


def fib_while(n):
    first = 0
    second = 1
    temp_number = first + second
    count = 2
    while count < n:
        first, second = second, temp_number
        temp_number = first + second
        count += 1
    print(temp_number)

start = time.perf_counter()
fib_while(6)
end = time.perf_counter()
duration2 = end - start

print(duration1/duration2)