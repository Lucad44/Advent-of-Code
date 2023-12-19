import re


ans = 0
with open("2023/input.txt", "r") as f:
    for line in f:
        winning = [int(x) for x in re.findall(r'\d+', line[10:line.index('|') - 1])]
        have = [int(x) for x in re.findall(r'\d+', line[line.index('|') + 2:])]
        res = -1
        for n in have:
            res += winning.count(n)
        if res != -1:
            ans += 2**res
print(ans)
