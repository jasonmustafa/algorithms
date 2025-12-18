import sys


def set_digit(ij: int, bank: list[str], l: int, r: int) -> int:
    cur_joltage = joltages[ij]

    for i in range(l, r + 1):
        joltage = bank[i]

        if int(joltage) > int(cur_joltage):
            joltages[ij] = joltage
            cur_joltage = joltage
            new_l = i + 1

    return new_l


file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

with open(input_file_name, "r") as f:
    banks = [line.rstrip() for line in f]

total_joltage = 0

for bank in banks:
    joltages = ["0"] * 12
    len_window = len(bank) - 12

    l = 0
    r = l + len_window

    for i in range(12):
        l = set_digit(i, bank, l, r)
        remaining = 12 - i - 1
        r = len(bank) - remaining

    bank_joltage = int("".join(joltages))
    total_joltage += bank_joltage

print(total_joltage)
