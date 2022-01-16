# Say that you are a traveller on a 3 d grid begin from top left corner to bottom  right .you may only move down or right
# how many ways can you travel to the goal on a grid with m*n
# brut force
# def min_no_of_ways(m, n):
#     if m == 1 and n == 1:
#         return 1
#     if m == 0 or n == 0:
#         return 0
#     return min_no_of_ways(m - 1, n) + min_no_of_ways(m, n - 1)
#
#
# print(min_no_of_ways(0, 0))
# print(min_no_of_ways(2,3))
# print(min_no_of_ways(10, 20))

# dynamic programming


def dyn_min_no_of_ways(m, n,map = {}):
    key = str(m), "T", str(n)
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    if key in map:
        return map[key]
    map[key] = dyn_min_no_of_ways(m - 1, n) + dyn_min_no_of_ways(m, n - 1)
    return map[key]


print(dyn_min_no_of_ways(10, 10))

