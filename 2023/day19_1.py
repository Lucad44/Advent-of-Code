workflows = {}
parts = []

with open("2023/input.txt", "r") as f:
    for line in f:
        line = line.rstrip()
        if not line:
            continue
        elif line[0] != '{':
            key = line[:line.index('{')]
            val = line[line.index('{') + 1:-1].split(',')
            workflows[key] = val
        else:
            parts.append({x[0]: int(x[2:]) for x in line[1:-1].split(',')})

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
for i, part in enumerate(parts):
    if flow("in", i):
        for v in part.values():
            ans += v 
print(ans)