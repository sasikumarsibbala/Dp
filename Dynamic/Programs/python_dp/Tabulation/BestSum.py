def best_sum(target, array):
    a = [None] * (target + 1)
    a[0] = []
    for i in range(target + 1):
        if a[i] is not None:
            for num in array:
                combi = [*a[i], num]
                if i + num < len(a):
                    if a[i + num] is None or len(a[i]) > len(combi):
                        a[i + num] = combi
    return a[target]


print(best_sum(100, [1,24,25]))
