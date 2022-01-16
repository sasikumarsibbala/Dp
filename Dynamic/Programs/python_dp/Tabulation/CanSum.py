def can_sum(target, array):
    a = [False] * (target + 1)
    a[0] = True
    for i in range(target + 1):
        if a[i]:
            for num in array:
                if i + num < len(a):
                    a[i + num] = True
    return a[target]


print(can_sum(7, [5, 3, 4]))
print(can_sum(7, [2, 3]))
print(can_sum(300, [7, 14]))
