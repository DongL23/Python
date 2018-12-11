# Uses python3
def calc_fib(n):
    l = [0, 1]
    if n < 2:
        return l[n]
    for i in range(2, n+1):
        l.append(l[i-2]+l[i-1])
        # print(l)
    return l[-1]


n = int(input())
print(calc_fib(n))
