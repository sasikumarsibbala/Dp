# write function to return all 2d array string taking input as target and array  of string
def all_construct(target, array):
    if target == "": return [[]]
    result = []
    for word in array:
        try:
            if target.index(word) == 0:
                remaining_string = target[len(word):]
                others_ways = all_construct(remaining_string, array)
                target_ways = list(map(lambda ways:[word,*ways])
                result.append(*target_ways)
        except:
            continue


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
