instructions = []
with open("2023/input.txt", "r") as f:
    for line in f:
        line = line.split()[2]
        instructions.append((int(line[2:7], 16), int(line[7:-1])))

last_pos = [0, 0]
vertices = [last_pos.copy()]
perimeter = 0

for x, d in instructions:
    match d:
        case 0:
            last_pos[1] += x
        case 2:
            last_pos[1] -= x
        case 3:
            last_pos[0] -= x
        case 1:
            last_pos[0] += x
    perimeter += x
    vertices.append(last_pos.copy())

ans = vertices[-1][0] * vertices[0][1] - vertices[-1][1] * vertices[0][0]
for i in range(1, len(vertices)):
    ans += vertices[i - 1][0] * vertices[i][1] - vertices[i - 1][1] * vertices[i][0]

ans  = abs(ans) // 2
ans += perimeter // 2 + 1
print(ans)
