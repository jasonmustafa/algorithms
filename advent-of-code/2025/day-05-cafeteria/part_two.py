import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

with open(input_file_name, "r") as f:
    data = f.read().splitlines()

fresh_id_ranges = []

for row in data:
    if row == "":
        break

    lo, hi = row.split("-")
    fresh_id_ranges.append((int(lo), int(hi)))

num_fresh_ids = 0
unique_ranges = []

for lo, hi in fresh_id_ranges:
    i = 0

    while i < len(unique_ranges):
        c_lo, c_hi = unique_ranges[i]

        # ranges overlap
        if c_lo <= lo and c_hi >= lo or lo <= c_lo and hi >= c_lo:
            lo = min(lo, c_lo)
            hi = max(hi, c_hi)
            del unique_ranges[i]
            continue

        i += 1

    unique_ranges.append((lo, hi))


for lo, hi in unique_ranges:
    num_fresh_ids += hi - lo + 1

print(num_fresh_ids)
