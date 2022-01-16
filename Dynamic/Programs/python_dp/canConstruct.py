# Problem
#
# write a fucntion canConstruct(target,string array)
# return Boolean input string can be constructed by elements in string array
# brut force
# time-n^m*m
# space m*m=
# def can_construct(target, array):
#     if target == "": return True
#     for word in array:
#         try:
#             if target.index(word) == 0:
#                 suffix = target[len(word):]
#                 if can_construct(suffix, array):
#                     return True
#         except:
#             continue
#     return False

# memoryization:
#time- n*m2
#spa
def can_construct(target, array, map={}):
    if target in map: return map[target]
    if target == "": return True
    for word in array:
        try:
            if target.index(word) == 0:
                suffix = target[len(word):]
                if can_construct(suffix, array):
                    map[target] = True
                    return True
        except:
            continue
    map[target] = False
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('skateboard', ['skate', 'ls', 'ms', 'wd']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                    ['e', 'ee', 'eee', 'eeeee', 'eeeeee', 'eeeeeee', 'eeeeeeeeee']))
