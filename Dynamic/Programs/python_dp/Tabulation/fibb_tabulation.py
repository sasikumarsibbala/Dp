# fibbnaci number using tabulation
def fib(n):
    a = [0] * (n + 2)
    a[1] = 1
    for i in range(0, n):
        a[i + 1] = a[i + 1] + a[i]
        a[i + 2] = a[i + 2] + a[i]

    return a[n+1]


print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))
