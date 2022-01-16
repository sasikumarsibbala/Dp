# def fib(n):
#     f = [0, 1]
#     for i in range(2,n+1):
#         f.append(f[i-1]+f[i-2])
#     return f[n]
#
#
# print(fib(100000))

n = int(input("please give a number for fibonacci series : "))


def fibonacci(num):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


print("fibonacci series are : ")
for i in range(0, n):
    print(fibonacci(i))
