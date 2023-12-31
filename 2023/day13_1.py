import numpy as np


with open("2023/input.txt", "r") as f:
    patterns = f.read().split("\n\n")

def find_reflection(arr):
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]: 
            l, r = i - 2, i + 1
            valid = True
            while l >= 0 and r < len(arr):
                if arr[l] != arr[r]:
                    valid = False
                    break
                l -= 1
                r += 1
            if valid:
                return i
    return -1

ans = 0
for pattern in patterns:
    grid = np.array([list(x) for x in pattern.split()])
    rows = []
    for row in grid:
        rows.append(''.join(['0' if ch == '.' else '1' for ch in row]))
    rows = [int(x, 2) for x in rows]
    cols = []
    for col in grid.T:
        cols.append(''.join(['0' if ch == '.' else '1' for ch in col]))
    cols = [int(x, 2) for x in cols]
    h_refl = find_reflection(rows)
    v_refl = find_reflection(cols)
    if h_refl != -1:
        ans += h_refl * 100
    else:
        ans += v_refl

print(ans)



