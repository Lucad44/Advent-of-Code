import sys


with open("2023/input.txt", "r") as f:
    lines = f.read().splitlines()

m, n = len(lines), len(lines[0])
sys.setrecursionlimit(10**4)
energised = [set() for _ in range(m) for _ in range(n)]
energised = [energised[i * n:(i + 1) * n] for i in range(m)]

def energise(i, j, dir):
    if i < 0 or i >= m or j < 0 or j >= n or dir in energised[i][j]:
        return 0
    was_empty = not len(energised[i][j])
    energised[i][j].add(dir)
    match lines[i][j]:
        case '.':
            if dir == "left":
                return was_empty + energise(i, j - 1, "left")
            elif dir == "right":
                return was_empty + energise(i, j + 1, "right")
            elif dir == "up":
                return was_empty + energise(i - 1, j, "up")
            elif dir == "down":
                return was_empty + energise(i + 1, j, "down")
        case '/':
            if dir == "left":
                return was_empty + energise(i + 1, j, "down")  
            elif dir == "right":
                return was_empty + energise(i - 1, j, "up")
            elif dir == "up":
                return was_empty + energise(i, j + 1, "right")
            elif dir == "down":
                return was_empty + energise(i, j - 1, "left")
        case '\\':
            if dir == "left":
                return was_empty + energise(i - 1, j, "up")
            elif dir == "right":
                return was_empty + energise(i + 1, j, "down")
            elif dir == "up":
                return was_empty + energise(i, j - 1, "left")
            elif dir == "down":
                return was_empty + energise(i, j + 1, "right")
        case '|':
            if dir == "left" or dir == "right":
                return was_empty + energise(i - 1, j, "up") + energise(i + 1, j, "down")
            elif dir == "up":
                return was_empty + energise(i - 1, j, "up")
            elif dir == "down":
                return was_empty + energise(i + 1, j, "down")
        case '-':
            if dir == "left":
                return was_empty + energise(i, j - 1, "left")
            elif dir == "right":
                return was_empty + energise(i, j + 1, "right")
            elif dir == "up" or dir == "down":
                return was_empty + energise(i, j - 1, "left") +energise(i, j + 1, "right")


print(energise(0, 0, "right"))