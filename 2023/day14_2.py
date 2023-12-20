with open("2023/input.txt", "r") as f:
    lines = [list(line) for line in f.read().rsplit()]

def tilt(direction):
    match direction:
        case "north":
            for i, line in enumerate(lines):
                for ci, ch in enumerate(line):
                    if ch == 'O':
                        lines[i][ci] = '.'
                        j = i - 1
                        while j >= 0 and lines[j][ci] == '.': 
                            j -= 1
                        lines[j + 1][ci] = 'O'
        case "south":
            for i in range(len(lines) - 1, -1, -1):
                for ci, ch in enumerate(lines[i]):
                    if ch == 'O':
                        lines[i][ci] = '.'
                        j = i + 1
                        while j < len(lines) and lines[j][ci] == '.': 
                            j += 1
                        lines[j - 1][ci] = 'O'
        case "west":
            for i, line in enumerate(lines):
                for ci, ch in enumerate(line):
                    if ch == 'O':
                        lines[i][ci] = '.'
                        j = ci - 1
                        while j >= 0 and lines[i][j] == '.': 
                            j -= 1
                        lines[i][j + 1] = 'O'
        case "east":
            for i, line in enumerate(lines):
                for ci in range(len(line) - 1, -1, -1):
                    if line[ci] == 'O':
                        lines[i][ci] = '.'
                        j = ci + 1
                        while j < len(line) and lines[i][j] == '.': 
                            j += 1
                        lines[i][j - 1] = 'O'

results = []
while 1:
    for direction in ("north", "west", "south", "east"):
        tilt(direction)
    ans = 0
    for i in range(-len(lines), 0, 1):
        for ch in lines[i]:
            if ch == 'O':
                ans += -i
    if results.count(ans) > 2:
        print(ans)
        break
    results.append(ans)