import re


with open("2023/input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

dict_list = []
for i, line in enumerate(lines):
    matches = [(int(match.group()), match.start(), match.end() - 1) for match in re.finditer(r'\d+', line)]
    num_dict = {}
    for num, start, end in matches:
        if num not in num_dict:
            num_dict[num] = []
        num_dict[num].extend([start, end])
    dict_list.append(num_dict)

ans = 0
for i, line in enumerate(lines):
    for j in range(len(line)):
        coords = []
        if line[j] == '*':
            if j and line[j - 1].isdigit():
                coords.append(j - 1)
            if j < len(line) - 1 and line[j + 1].isdigit():
                coords.append(j + 1)

            up_bounds, down_bounds = True, True
            flags = [True, True]
            index = 0
            up, down = max(0, j - 1), max(0, j - 1)
            end = min(len(line), j + 2)
            while up < end or down < end:
                if (up >= end):
                    up_bounds = False
                if (down >= end):
                    down_bounds = False
                if up_bounds and True in flags and i and lines[i - 1][up].isdigit():
                    coords.append(up)
                    flags[index] = False
                    index += 1
                    while up < len(line) and lines[i - 1][up].isdigit():
                        up += 1
                        continue
                if down_bounds and True in flags and i < len(lines) - 1 and lines[i + 1][down].isdigit():
                    coords.append(down)
                    flags[index] = False
                    index += 1
                    while down < len(line) and lines[i + 1][down].isdigit():
                        down += 1
                        continue
                up += 1
                down += 1

        if len(coords) != 2:
            continue
        
        print_n = []
        prod = 1
        for l, d in enumerate(dict_list):
            if l < i - 1:
                continue
            if l > i + 1:
                break
            for k, v in d.items():
                for t in range(0, len(v), 2):
                    if (v[t] <= coords[0] <= v[t + 1]) or (v[t] <= coords[1] <= v[t + 1]):
                        print_n.append(k)
                        prod *= k
        ans += prod
        print(i, print_n[0], "*", print_n[1], "prod: ", prod)
        print("ans: ", ans)

print(ans)
