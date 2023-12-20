from itertools import product


workflows = {}

with open("2023/input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        if not line:
            break
        key = line[:line.index('{')]
        val = line[line.index('{') + 1:-1].split(',')
        workflows[key] = val

def flow(workflow, i):
    for item in workflows[workflow]:
        if item == 'A':
            return True
        elif item == 'R':
            return False
        if item.count(':') > 0:
            sections = item.split(':')
            if eval(f'parts[{i}]["{sections[0][0]}"]{sections[0][1:]}'):
                if sections[1] == 'A':
                    return True
                elif sections[1] == 'R':
                    return False
                return flow(sections[1], i)
        else:
            return flow(item, i)
                    
ans = 0
for combo in product(range(1, 4001), repeat=4):
    parts = [{'x': combo[0], 'm': combo[1], 'a': combo[2], 's': combo[3]}]
    ans += flow("in", 0)
print(ans)