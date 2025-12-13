import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

f = open(input_file_name, "r")
id_ranges = f.read().strip().split(",")
f.close()

invalid_ids = []


def check_id(id: str) -> None:
    if id.startswith("0"):
        return

    m = len(id) // 2
    seq_1 = id[:m]
    seq_2 = id[m:]

    if seq_1 == seq_2:
        invalid_ids.append(int(id))


for id_range in id_ranges:
    ids = id_range.split("-")
    first = int(ids[0])
    last = int(ids[1])

    id = first
    while id <= last:
        check_id(str(id))
        id += 1

print(sum(invalid_ids))
