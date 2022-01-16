# take array and sum as input return the combnination are possible array
# brut force
# def howsum(tatgetSum, array):
#     if tatgetSum == 0:
#         return []
#     if tatgetSum < 0:
#         return None
#     for num in array:
#         rem = tatgetSum - num
#         rem1 = howsum(rem, array)
#         if rem1 is not None:
#             return [*rem1, num]
#
#     return None
# memorization:
def howsum(tatgetSum, array, map={}):
    if tatgetSum in map:
        return map[tatgetSum]
    if tatgetSum == 0: return []
    if tatgetSum < 0:
        return None
    for num in array:

        rem = tatgetSum - num
        rem1 = howsum(rem, array)
        if rem1 is not None:
            map[tatgetSum] = [*rem1, num]
            return map[tatgetSum]

    map[tatgetSum] = None
    return None


print(howsum(7, [3, 3]))
print(howsum(7, [2, 4]))
print(howsum(300, [7, 14]))
