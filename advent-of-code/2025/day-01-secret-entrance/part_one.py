import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

f = open(input_file_name, "r")
rotations = f.read().splitlines()
print(rotations)

password = 0
dial = 50
print(f"dial started at == {dial} ==")

for r in rotations:
    direction = r[0]
    distance = int(r[1:])

    if direction == "L":
        distance *= -1

    dial = (dial + distance) % 100

    password += dial == 0
    print(f"dial is at == {dial} ==")
    print(f"dial is rotated == {r} ==")

print(f"{password=}")
