import re

input_string = ".......12.......935............184.720...243........589.652..........435..........483.............6...................904.......904..........."

# Use a regular expression to find all numbers and their indices in the string
matches = [(int(match.group()), match.start(), match.end() - 1) for match in re.finditer(r'\d+', input_string)]

# Create a dictionary with number as key and a list of starting and ending indices interleaved as value
number_dict = {}
for num, start, end in matches:
    if num not in number_dict:
        number_dict[num] = []
    number_dict[num].extend([start, end])

print(number_dict)
