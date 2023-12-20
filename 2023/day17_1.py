from functools import cache
from sys import setrecursionlimit


graph = []
with open("2023/input.txt", "r") as f:
    for line in f:
        line = line.rsplit()
        graph.append([int(x) for x in line[0]])
m, n = len(graph), len(graph[0])

def dfs(row, col, direction, steps):
    if row < 0 or row >= m or col < 0 or col >= n or (row, col) in visited:
        return float('inf')
    elif row == m - 1 and col == n - 1:
        return graph[-1][-1]
    visited.add((row, col))
    res = graph[row][col]
    if direction == "left" or direction == "right":
        turn = min(dfs(row - 1, col, "up", 2), dfs(row + 1, col, "down", 2))
        if direction == "left":
            straight = float('inf') if steps == 0 else dfs(row, col - 1, "left", steps - 1)
        else:
            straight = float('inf') if steps == 0 else dfs(row, col + 1, "right", steps - 1)
        res += min(turn, straight)
    else:
        turn = min(dfs(row, col - 1, "left", 2), dfs(row, col + 1, "right", 2))
        if direction == "up":
            straight = float('inf') if steps == 0 else dfs(row - 1, col, "up", steps - 1)
        else:
            straight = float('inf') if steps == 0 else dfs(row + 1, col, "down", steps - 1)
        res += min(turn, straight)
    visited.remove((row, col))
    return res

setrecursionlimit(10**6)
ans = float('inf')
for d in ("right", "down"):
    visited = set()
    ans = min(ans, dfs(1, 0, d, 2), dfs(0, 1, d, 2))
ans -= (graph[0][0] + graph[1][0])
print(ans)
