import re


def is_symbol(c):
    if ('!' <= c <= '/' and c != '.') or (':' <= c <= '@') or ('[' <= c <= '`') or ('{' <= c <= '~'):
        return True
    return False

with open("input.txt", "r") as f:
    lines = [line.rstrip() for line in f]

ans = 0
for i in range(len(lines)):
    matches = [(int(match.group()), match.start(), match.end() - 1) for match in re.finditer(r'\d+', lines[i])]
    num_dict = {}
    for num, start, end in matches:
        if num not in num_dict:
            num_dict[num] = []
        num_dict[num].extend([start, end])

    for k, v in num_dict.items():
        for t in range(0, len(v), 2):
            if (v[0] and is_symbol(lines[i][v[0] - 1])) or (v[1] < len(lines[i]) - 1 and is_symbol(lines[i][v[1] + 1])):
                print(k, v[t], v[t + 1])
                ans += k
                continue
            for l in range(max(0, v[t] - 1), min(len(lines[i]), v[t + 1] + 2)):
                if ((i and is_symbol(lines[i - 1][l])) or (i < len(lines) - 1 and is_symbol(lines[i + 1][l]))):
                    print(k, v[t], v[t + 1])
                    ans += k
                    break

print(ans)
