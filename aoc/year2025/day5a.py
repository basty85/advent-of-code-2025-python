from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day5.txt"


def read_input() -> list[str]:
    """Read and parse the complete input file into a list of strings."""
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f.readlines()]


def process_input(input: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = []
    ids = []
    iterator = iter(input)

    # Extract id ranges
    for line in iterator:
        if not line.strip():
            break
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    # Extract specific ids
    for line in iterator:
        ids.append(int(line.strip()))

    return ranges, ids


def main() -> None:
    id_ranges = []
    ids = []
    count = 0

    my_input = read_input()
    id_ranges, ids = process_input(my_input)

    id_set = set(ids)
    seen = set()
    count = 0

    for start, end in id_ranges:
        for j in range(start, end + 1):
            if j in id_set and j not in seen:
                count += 1
                   seen.add(j)


if __name__ == "__main__":
    main()
