def validate(springs, nums):
    if '?' in springs:
        return 0
    springs = springs.split(".")
    springs = [x for x in springs if x != ""]
    if len(springs) != len(nums):
        return 0
    for i, s in enumerate(springs):
        if s != '#' * nums[i]:
            return 0
    return 1

ans = [0]

def backtrack(i, springs, nums):
    if i == len(springs):
        return
    if springs[i] == '?':
        springs[i] = '.'
        ans[0] += validate(''.j oin(springs), nums)
        backtrack(i + 1, springs, nums)
        springs[i] = '#'
        ans[0] += validate(''.join(springs), nums)
        backtrack(i + 1, springs, nums)
        springs[i] = '?'
    else:
        backtrack(i + 1, springs, nums)


with open("2023/input.txt", "r") as f:
    for line in f:
        springs, nums = line.split()
        nums = [int(x) for x in nums.split(",")]
        springs  = '?'.join(([springs] * 5))
        nums *= 5
        backtrack(0, list(springs), nums)

print(ans)