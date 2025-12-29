import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

with open(input_file_name, "r") as f:
    grid = [list(line.rstrip()) for line in f]

rows = len(grid)
cols = len(grid[0])


def check_roll(r, c):
    if grid[r][c] != "@":
        return False

    up = (r - 1, c)
    down = (r + 1, c)
    left = (r, c - 1)
    right = (r, c + 1)

    up_left = (r - 1, c - 1)
    down_left = (r + 1, c - 1)
    up_right = (r - 1, c + 1)
    down_right = (r + 1, c + 1)

    adjacents = [up, down, left, right, up_left, down_left, up_right, down_right]
    num_adj_rolls = 0

    for rr, cc in adjacents:
        # outside grid
        if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
            continue

        if grid[rr][cc] == "@":
            num_adj_rolls += 1

    return num_adj_rolls < 4


accessible_rolls = []

for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if check_roll(r, c):
            accessible_rolls.append((r, c))

for r, c in accessible_rolls:
    grid[r][c] = "X"

print(len(accessible_rolls))
