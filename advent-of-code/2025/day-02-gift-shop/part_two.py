import sys

file_to_use = sys.argv[1]
input_file_name = "input.txt" if file_to_use == "input" else "example.txt"

f = open(input_file_name, "r")
id_ranges = f.read().strip().split(",")
f.close()

invalid_ids = []


# >= 3 because sequence repeats at least twice
# split returns empty string before, after, and between two occurrences
def id_repeats_sequence(id: str, seq: str) -> bool:
    splits = id.split(seq)
    return len(splits) >= 3 and set(splits) == {""}


def check_id(id: str) -> None:
    if id.startswith("0"):
        return

    l = 0
    r = 0
    m = len(id) // 2

    while r <= m:
        seq = id[l : r + 1]

        if id_repeats_sequence(id, seq):
            invalid_ids.append(int(id))
            return

        r += 1


for id_range in id_ranges:
    ids = id_range.split("-")
    first = int(ids[0])
    last = int(ids[1])

    id = first

    while id <= last:
        check_id(str(id))
        id += 1

print(sum(invalid_ids))
