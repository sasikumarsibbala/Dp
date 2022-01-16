# print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))


def can_construct(target, array):
    table = [False] * (len(target) + 1)
    table[0] = True
    for i in range(len(table)):
        if table[i]:
            for num in array:
                if target[i:i + len(num)] == num:
                    if (i + len(num)) < len(table):
                        table[i + len(num)] = True

    return table[len(target)]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['eeee', 'eeeeeeeee', 'eeeeeeeeeeeeeee','eeeeeeeeeeeeeeeee']))
