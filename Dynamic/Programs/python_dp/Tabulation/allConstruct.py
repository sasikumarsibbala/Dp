def all_construct(target, word_bank):
    table = [[]] * (len(target) + 1)
    table[0] = [[]]
    for i in range(len(table)):
        for word in word_bank:
            if target[i:i + len(word)] == word:
                newComb = map(table[i], lambda sub: [*sub, word])


print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
