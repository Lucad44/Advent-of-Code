import sys


with open("2023/input.txt", "r") as f:
    lines = f.read().splitlines()

m, n = len(lines), len(lines[0])
energised = [set() for _ in range(m) for _ in range(n)]
energised = [energised[i * n:(i + 1) * n] for i in range(m)]
sys.setrecursionlimit(10**6)

def energise(i, j, dir):
    if i < 0 or i >= m or j < 0 or j >= n or dir in energised[i][j]:
        return
    energised[i][j].add(dir)
    match lines[i][j]:
        case '.':
            if dir == "left":
                energise(i, j - 1, "left")
            elif dir == "right":
                energise(i, j + 1, "right")
            elif dir == "up":
                energise(i - 1, j, "up")
            elif dir == "down":
                energise(i + 1, j, "down")
        case '/':
            if dir == "left":
                energise(i + 1, j, "down")  
            elif dir == "right":
                energise(i - 1, j, "up")
            elif dir == "up":
                energise(i, j + 1, "right")
            elif dir == "down":
                energise(i, j - 1, "left")
        case '\\':
            if dir == "left":
                energise(i - 1, j, "up")
            elif dir == "right":
                energise(i + 1, j, "down")
            elif dir == "up":
                energise(i, j - 1, "left")
            elif dir == "down":
                energise(i, j + 1, "right")
        case '|':
            if dir == "left" or dir == "right":
                energise(i - 1, j, "up")
                energise(i + 1, j, "down")
            elif dir == "up":
                energise(i - 1, j, "up")
            elif dir == "down":
                energise(i + 1, j, "down")
        case '-':
            if dir == "left":
                energise(i, j - 1, "left")
            elif dir == "right":
                energise(i, j + 1, "right")
            elif dir == "up" or dir == "down":
                energise(i, j - 1, "left")
                energise(i, j + 1, "right")
                

energise(0, 0, "right")
ans = 0
for line in energised:
    print(line)
    for x in line:
        if x:
            ans += 1
print(ans)