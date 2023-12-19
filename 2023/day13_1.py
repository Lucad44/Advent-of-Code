import numpy as np


with open("2023/input.txt", "r") as f:
    patterns = f.read().split("\n\n")

ans = 0
for pattern in patterns:
    grid = np.array([list(x) for x in pattern.split()])
    v_refl = {}
    for i in range(1, grid.shape[1]):
        if np.array_equal(grid[:, i], grid[:, i - 1]):
            v_refl[i] = True
    h_refl = {}
    for i in range(1, grid.shape[0]):
        if np.array_equal(grid[i], grid[i - 1]):
            h_refl[i] = True
    
    for k in v_refl.keys():
        for l, r in zip(range(k, grid.shape[1]), range(k - 1, -1, -1)):
            if not np.array_equal(grid[:, l], grid[:, r]):
                v_refl[k] = False
                break

    for k in h_refl.keys():
        for l, r in zip(range(k, grid.shape[0]), range(k - 1, -1, -1)):
            if not np.array_equal(grid[l], grid[r]):
                h_refl[k] = False
                break
    print(v_refl, h_refl)
    for k, v in v_refl.items():
        if v:
            ans += k
    for k, v in h_refl.items():
        if v:
            ans += k * 100
print(ans)
