import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

with open(input_file_name, "r") as f:
    banks = [line.rstrip() for line in f]

total_joltage = 0

for bank in banks:
    li = -1
    lj = 0
    rj = 0

    for i in range(len(bank) - 1):
        joltage = int(bank[i])

        if joltage > lj:
            li = i
            lj = joltage

    for i in range(li + 1, len(bank)):
        joltage = int(bank[i])
        if joltage > rj:
            rj = joltage

    bank_joltage = int(f"{lj}{rj}")
    total_joltage += bank_joltage

print(total_joltage)
