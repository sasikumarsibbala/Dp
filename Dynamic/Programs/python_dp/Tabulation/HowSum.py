def how_sum(target, array):
    a = [None] * (target + 1)
    a[0] = []
    for x in range(0, target):
        if a[x] is not None:
            for num in array:
                if x + num < len(a):
                    a[x + num] = [*a[x], num]
    return a[target]


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(300, [7, 14]))
