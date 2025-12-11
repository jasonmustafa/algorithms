import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

f = open(input_file_name, "r")
rotations = f.read().splitlines()
print(rotations)

password = 0
dial = 50
print(f"the dial starts by pointing at ** {dial} **")

for r in rotations:
    direction = r[0]
    distance = int(r[1:])

    # add number of full rotations
    password += distance // 100
    distance %= 100

    if direction == "L":
        distance *= -1

    turns_left_past_0 = direction == "L" and dial + distance <= 0 and dial != 0
    turns_right_past_99 = direction == "R" and dial + distance >= 100

    if turns_left_past_0 or turns_right_past_99:
        password += 1

    dial = (dial + distance) % 100
    print(f"the dial is rotated ** {r} ** to point at ** {dial} **")

print(f"{password=}")
