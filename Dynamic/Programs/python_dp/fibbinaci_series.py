# memorization
map={}
def fib(num):
    if num in map:
        return map[num]
    if num <= 2:
        return 1
    map[num] = fib(num - 1) + fib(num - 2)
    return map[num]


print(fib(4))
print(fib(6))
print(fib(7))
print(fib(8))
