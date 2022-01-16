# # Python 3 program of above approach
#
# # A utility function to get max
# # of two egers
#
#
# # Returns the length of the longest
# # palindromic subsequence in seq
# def lps(seq, i, j):
#     # Base Case 1: If there is
#     # only 1 character
#     if i == j:
#         return 1
#
#     # Base Case 2: If there are only 2
#     # characters and both are same
#     if seq[i] == seq[j] and i + 1 == j:
#         return 2
#
#     # If the first and last characters match
#     if seq[i] == seq[j]:
#         return lps(seq, i + 1, j - 1) + 2
#
#     # If the first and last characters
#     # do not match
#     return max(lps(seq, i, j - 1),
#                lps(seq, i + 1, j))
#
#
# # Driver Code
# if __name__ == '__main__':
#     seq = "abcd"
#     n = len(seq)
#     print("The length of the LPS is",
#           lps(seq, 0, n - 1))
#
#
# def longest_sub_sequence(s):
#     if len(s) < 2:
#         return len(s)
#     table = [[0 for _ in s] for _ in s]
#     for i in range(len(table)):
#         table[i][i] = 1
#
#     for start in range(1, len(table)):
#         right = start
#         for left in range(len(table) - start):
#             if s[left] == s[right]:
#                 table[left][right] = 2 + table[left + 1][right - 1]
#             else:
#                 table[left][right] = max(table[left][right - 1], table[left + 1][right])
#             right += 1
#     return table[0][-1]
#
#
# print(longest_sub_sequence("abcb"))

def pract_longest_sub_sequence(s):
    if len(s) < 2:
        return len(s)
    dp = [[0 for _ in s] for _ in s]
    for i in range(len(dp)):
        dp[i][i] = 1
    for start in range(1, len(dp)):
        right = start
        for left in range(len(dp) - start):
            if s[left] == s[right]:
                dp[left][right] = 2 + dp[left + 1][right - 1]
            else:
                dp[left][right] = max(dp[left][right - 1], dp[left + 1][right])
            right += 1
    return dp[0][-1]


print(pract_longest_sub_sequence(""))
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         if len(s) < 2:
#             return len(s)
#         dp = [[0 for _ in s] for _ in s]
#         for i in range(len(dp)):
#             dp[i][i] = 1
#         for start in range(1, len(dp)):
#             right = start
#             for left in range(len(dp) - start):
#                 if s[left] == s[right]:
#                     dp[left][right] = 2 + dp[left + 1][right - 1]
#                 else:
#                     dp[left][right] = max(dp[left][right - 1], dp[left + 1][right])
#                 right += 1
#         return dp[0][-1]
