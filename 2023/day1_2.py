with open("input.txt", "r") as f:
    lines = f.read().splitlines()

digits_string = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits = ['one1one', 'two2two', 'three3three', 'four4four', 'five5five', 'six6six', 'seven7seven', 'eight8eight', 'nine9nine']

with open("input_edit.txt", "w") as f:
    for line in lines:
        new_line = line
        for i in range(9):
            new_line = new_line.replace(digits_string[i], digits[i])
        f.write(new_line + '\n')