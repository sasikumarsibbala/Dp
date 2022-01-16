# # Write a function 'canSum(targetSum,numbers) that target sum and array as a  parameter as  arguments
# # return a boolean whether is it possible to generate target sum using numbers from Array
# # all input values are non-negative
# # brute Force
#
#
# # def canSum(targetSum, numbers):
# #     if targetSum == 1:
# #         return True
# #     if targetSum == 0:
# #         return False
# #     for num in numbers:
# #         value = targetSum - num
# #         if canSum(value, numbers):
# # #             return True
# # #     return False
# # def canSum(targetSum, Array, map={}):
# #     if targetSum in map:
# #         return map[targetSum]
# #     if targetSum < 0:
# #         return False
# #     if targetSum == 0:
# #         return True
# #     for num in Array:
# #         keys = targetSum - num
# #         if canSum(keys, Array):
# #             map[targetSum] = True
# #             return True
# #     map[targetSum] = False
# #     return False
# #
# #
# # print(canSum(6, [2, 3]))
# # print(canSum(7, (5, 3, 4, 7)))
# # print(canSum(7, [2, 4]))
# # print(canSum(8, [2, 3, 5]))
# # print(canSum(50, [7, 14]))
# # # import sys
# # # print(sys.getrecursionlimit())
#
# def isSubsetSum(set, n, sum):
#
#     # Base Cases
#     if sum == 0:
#         return True
#     if n == 0:
#         return False
#
#     # If last element is greater than
#     # sum, then ignore it
#     if set[n - 1] > sum:
#         return isSubsetSum(set, n - 1, sum)
#
#     # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element
#     return isSubsetSum(
#         set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])
#
#
# # Driver code
# set = [2, 4]
# sum = 1000
# n = len(set)
# if isSubsetSum(set, n, sum):
#     print("Found a subset with given sum")
# else:
#     print("No subset with given sum")
#
# Python program for the above approach

# Taking the matrix as globally
tab = [[-1 for i in range(2000)] for j in range(2000)]


# Check if possible subset with
# given sum is possible or not
def subsetSum(a, n, sum,map={}):
    # If the sum is zero it means
    # we got our expected sum
    if sum == 0:return 1

    if n <= 0:
        return 0

    # If the value is not -1 it means it
    # already call the function
    # with the same value.
    # it will save our from the repetition.
    if tab[n - 1][sum] != -1:
        return map[sum]

    # if the value of a[n-1] is
    # greater than the sum.
    # we call for the next value
    if (a[n - 1] > sum):
        tab[n - 1][sum] = subsetSum(a, n - 1, sum)
        return map[sum]
    else:

        # Here we do two calls because we
        # don't know which value is
        # full-fill our criteria
        # that's why we doing two calls
        tab[n - 1][sum] = subsetSum(a, n - 1, sum)
        return map[sum] or subsetSum(a, n - 1, sum - a[n - 1])

# Driver Code

n = 2
a = [1, 3]
sum = 5

if subsetSum(a, n, sum):
    print("YES")
else:
    print("NO")