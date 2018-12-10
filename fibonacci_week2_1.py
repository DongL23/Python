# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    for i in range(2, n):
        return calc_fib(i - 1) + calc_fib(i - 2)

n = int(input())
print(calc_fib(n))
