from collections import defaultdict
import re


seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

with open("2023/input.txt", "r") as f:
    seeds = [int(x) for x in re.findall(r'\d+', f.readline())]
    f.readline()
    current_map = None
    for line in f:
        line = line.strip()
        if line.endswith("map:"):
            current_map = line.split()[0].replace("-", "_")
        else:
            numbers = list(map(int, line.split()))
            getattr(locals()[f"{current_map}"], 'append')(numbers)

seed_to_soil.pop()
soil_to_fertilizer.pop()
fertilizer_to_water.pop()
water_to_light.pop()
light_to_temperature.pop()
temperature_to_humidity.pop()

def associate(original, seed, it):
    for r in it:
        if r[1] <= seed < r[1] + r[2]:
            diff = abs(seed - r[1])
            return r[0] + diff
    return seed

ans = float('inf')
for i in range(1, len(seeds), 2):
    print(i)
    for j in range(seeds[i - 1], seeds[i - 1] + seeds[i]):
        seed = j
        curr_seed = associate(seed, seed, seed_to_soil)
        curr_seed = associate(seed, curr_seed, soil_to_fertilizer)
        curr_seed = associate(seed, curr_seed, fertilizer_to_water)
        curr_seed = associate(seed, curr_seed, water_to_light)
        curr_seed = associate(seed, curr_seed, light_to_temperature)
        curr_seed = associate(seed, curr_seed, temperature_to_humidity)
        curr_seed = associate(seed, curr_seed, humidity_to_location)
        ans = min(ans, curr_seed)


print(ans)