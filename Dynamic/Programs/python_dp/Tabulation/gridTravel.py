# m = 4
# n = 5

# a = [[0 for x in range(n + 1)] for x in range(m + 1)]
# print(a)


def grid_travel(m, n):
    a = [[0 for x in range(n + 1)] for x in range(m + 1)]
    a[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            temp = a[i][j]
            if j + 1 <= n:
                a[i][j + 1] += temp

            if i + 1 <= m:
                a[i + 1][j] += temp

    return a[m][n]


#
print(grid_travel(1, 1))
print(grid_travel(2, 3))
print(grid_travel(3, 2))
print(grid_travel(3, 3))
print(grid_travel(18, 18))


# Python program to count all possible paths
# from top left to bottom right

# Returns count of possible paths to reach cell
# at row number m and column number n from the
# topmost leftmost cell (cell at 1, 1)
# def numberOfPaths(m, n):
    # Create a 2D table to store
    # results of subproblems
    # one-liner logic to take input for rows and columns
    # mat = [[int(input()) for x in range (C)] for y in range(R)]

    # count = [[0 for x in range(n)] for y in range(m)]
