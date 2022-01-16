def count_construct(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1
    for i in range(len(table)):
        for word in wordBank:
            if target[i:i + len(word)] == word:
                if i + len(word) < len(table):
                    table[i + len(word)] += table[i]
    return table[len(target)]


print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['eeee', 'eeeeeeeee', 'eeeeeeeeeeeeeee','eeeeeeeeeeeeeeeee']))

