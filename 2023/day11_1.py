import numpy as np


with open ("2023/input.txt", "r") as f:
    lines = f.read().splitlines()
    cosmo = np.array([list(line) for line in lines])
cosmo = np.insert(cosmo, np.where(np.all(cosmo == '.', axis=1))[0], '.', axis=0)
cosmo = np.insert(cosmo, np.where(np.all(cosmo == '.', axis=0))[0], '.', axis=1)

coords = {}
cnt = 1
for i in range(len(cosmo)):
    for j in range(len(cosmo[0])):
        if cosmo[i][j] == '#':
            coords[cnt] = (i, j)
            cnt += 1

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
