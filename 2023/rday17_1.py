lines = []
with open("2023/input.txt", "r") as f:
    for line in f:
        lines.append([int(x) for x in line.rstrip()])

for line in lines:
    print(line)

m, n = len(lines), len(lines[0])

def solve(i, j, dir, steps):
    if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
        return float('inf')
    if i == m - 1 and j == n - 1:
        return lines[i][j]
    visited[i][j] = True
    match dir:
        case "left":
            if steps == 3:
                return lines[i][j] + min(solve(i - 1, j, "up", 1), solve(i + 1, j, "down", 1))
            return lines[i][j] + min(solve(i, j - 1, "left", steps + 1), solve(i - 1, j, "up", 1), solve(i + 1, j, "down", 1))
        case "right":
            if steps == 3:
                return lines[i][j] + min(solve(i - 1, j, "up", 1), solve(i + 1, j, "down", 1))
            return lines[i][j] + min(solve(i, j + 1, "right", steps + 1), solve(i - 1, j, "up", 1), solve(i + 1, j, "down", 1))
        case "up":
            if steps == 3:
                return lines[i][j] + min(solve(i, j - 1, "left", 1), solve(i, j + 1, "right", 1))
            return lines[i][j] + min(solve(i - 1, j, "up", steps + 1), solve(i, j - 1, "left", 1), solve(i, j + 1, "right", 1))
        case "down":
            if steps == 3:
                return lines[i][j] + min(solve(i, j - 1, "left", 1), solve(i, j + 1, "right", 1))
            return lines[i][j] + min(solve(i + 1, j, "down", steps + 1), solve(i, j - 1, "left", 1), solve(i, j + 1, "right", 1))
        
visited = [[False] * n for _ in range(m)]
ans = solve(0, 0, "right", 1)
visited = [[False] * n for _ in range(m)]
print(min(ans, solve(0, 0, "down", 1)))
