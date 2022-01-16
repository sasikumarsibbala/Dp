# write a fucntion countConstruct that accepts a target and array of strings
# the function should return the no of  ways of that target string can be constructed by concatenating the strignarray elements
def countConstruct(target, array, map={}):
    if target in map: return map[target]
    value = 0
    if target == "": return True
    for arr in array:
        try:
            if target.index(arr) == 0:
                rem = target[len(arr):]
                no_of_ways_for_rest = countConstruct(rem, array)
                value = value + no_of_ways_for_rest
        except:
            continue
    map[target] = value
    return value


print(countConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(countConstruct('skateboard', ['bd', 'fsms', 'dsnsjns', 'dsmss']))
print(countConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                     ['eee', 'eeee', 'eeeee', 'eeeeeeeeeeee', 'eeeeeeeee']))
