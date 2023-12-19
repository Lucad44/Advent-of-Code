with open("2023/input.txt", "r") as f:
    lines = [list(line) for line in f.read().rsplit()]

for i, line in enumerate(lines):
    for ci, ch in enumerate(line):
        if ch == 'O':
            lines[i][ci] = '.'
            j = i - 1
            while j >= 0 and lines[j][ci] == '.': 
                j -= 1
            lines[j + 1][ci] = 'O'

for line in lines:
    print(''.join(line))

ans = 0
for i in range(-len(lines), 0, 1):
    for ch in lines[i]:
        if ch == 'O':
            ans += -i
print(ans)