def is_land_count(grid):
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited):
                count += 1
    return count


def explore(grid, r, c, visited):
    if grid[r][c] == 'W': return False
    key = str(r), ",", str(c)
    if key in visited: return False
    visited.add(key)
    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)
    return True


mat = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1]]
print(is_land_count(mat))
# print(len(mat[0]))
