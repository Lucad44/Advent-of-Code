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

            general_flag = True
            f1, f2 = True, True
            for l in range(max(0, j - 1), min(len(line), j + 2)):
                if f1 and i and lines[i - 1][l].isdigit():
                    coords.append(l)
                    f1 = False
                elif not f1 and i and lines[i - 1][l].isdigit() and not lines[i - 1][l - 1].isdigit():
                    general_flag = False
                    break
                if f2 and i < len(lines) -1 and lines[i + 1][l].isdigit():
                    coords.append(l)
                    f2 = False
                elif not f2 and i < len(lines) - 1 and lines[i + 1][l].isdigit() and not lines[i + 1][l - 1].isdigit():
                    general_flag = False
                    break

        if len(coords) != 2 or not general_flag:
            continue
        
        print(i, coords)

        prod = 1
        for l, d in enumerate(dict_list):
            if l < i - 1:
                continue
            if l > i + 1:
                break
            for k, v in d.items():
                for t in range(0, len(v), 2):
                    if (v[t] <= coords[0] <= v[t + 1]) or (v[t] <= coords[1] <= v[t + 1]):
                        prod *= k
        ans += prod

print(ans)
