lines = []
with open("2023/input.txt", "r") as f:
    for line in f:
        line = line.split()[:-1]
        line[-1] = int(line[-1])
        lines.append(line)

last_pos = [0, 0]
vertices = [last_pos.copy()]

for d, x in lines:
    match d:
        case 'R':
            last_pos[1] += x
        case 'L':
            last_pos[1] -= x
        case 'U':
            last_pos[0] -= x
        case 'D':
            last_pos[0] += x
    last_pos[0] *= -1
    vertices.append(last_pos.copy())
    last_pos[0] *= -1
    
for v in vertices:
    print(v)

ans = vertices[-1][0] * vertices[0][1] - vertices[-1][1] * vertices[0][0]
for i in range(1, len(vertices)):
    ans += vertices[i - 1][0] * vertices[i][1] - vertices[i - 1][1] * vertices[i][0]

ans //= 2
print(ans)
