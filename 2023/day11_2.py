import numpy as np


with open ("2023/input.txt", "r") as f:
    lines = f.read().splitlines()
    cosmo = np.array([list(line) for line in lines])

empty_rows = [i for i, line in enumerate(cosmo) if np.all(line == '.')]
empty_cols = [i for i in range(cosmo.shape[1]) if np.all(cosmo[:, i] == '.')]

expansion = 10**6
coords = {}
cnt = 1

for i in range(len(cosmo)):
    for j in range(len(cosmo[0])):
        if cosmo[i][j] == '#':
            coords[cnt] = [i, j]
            cnt += 1
for k, v in coords.items():
    cnt = 0
    for x in empty_rows:
        if v[0] > x:
            cnt += 1
    coords[k][0] += cnt * (expansion - 1)
    cnt = 0
    for x in empty_cols:
        if v[1] > x:
            cnt += 1
    coords[k][1] += cnt * (expansion - 1)


ans = 0
visited = set()
for k, v in coords.items():
    for k1, v1 in coords.items():
        if k1 == k:
            continue
        if tuple(sorted([k, k1])) not in visited:
            ans += abs(v[0] - v1[0]) + abs(v[1] - v1[1])
            visited.add(tuple(sorted([k, k1])))

print(ans) 