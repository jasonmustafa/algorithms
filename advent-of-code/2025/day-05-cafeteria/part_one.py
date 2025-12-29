import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

with open(input_file_name, "r") as f:
    data = f.read().splitlines()

for i, row in enumerate(data):
    # end of fresh id ranges
    if row == "":
        i_blank = i
        break

num_available_ids = 0

# loop through available ids
for id in data[i_blank + 1 :]:
    # loop through fresh id ranges
    for i in range(i_blank):
        lo, hi = data[i].split("-")
        lo = int(lo)
        hi = int(hi)

        if lo <= int(id) <= hi:
            num_available_ids += 1
            break

print(num_available_ids)
