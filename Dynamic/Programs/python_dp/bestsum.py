# brut force
# time O(n^m*m)
# space m2
# def bes_sum(target, array):
#     shortestCombination = None
#     if target == 0: return []
#     if target < 0: return None
#     for arr in array:
#         comb1 = target - arr
#         remainder = bes_sum(comb1, array)
#         if remainder is not None:
#             comination = [*remainder, arr]
#             if shortestCombination is None or len(comination) < len(shortestCombination):
#                 shortestCombination = comination
#
#     return shortestCombination

# memoryization
#time=m^2*n
#space(m^2)
def bes_sum(target, array, map={}):
    if target in map: return map[target]
    shortestCombination = None
    if target == 0: return []
    if target < 0: return None
    for arr in array:
        comb1 = target - arr
        remainder = bes_sum(comb1, array)
        if remainder is not None:
            comination = [*remainder, arr]
            if shortestCombination is None or len(comination) < len(shortestCombination):
                shortestCombination = comination

    map[target] = shortestCombination
    return map[target]


print(bes_sum(7, [3, 4, 7]))
print(bes_sum(8, [2, 3, 5]))
print(bes_sum(8, [1, 4, 5]))
print(bes_sum(100, [1, 2, 5, 25]))
