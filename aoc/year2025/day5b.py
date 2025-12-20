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
    # sort according to start value in ascending order
    id_ranges.sort(key=lambda x: x[0])

    merged = []
    current_start, current_end = id_ranges[0]

    for start, end in id_ranges[1:]:
        if start <= current_end + 1:  # overlapping or directly adjacent
            current_end = max(current_end, end)
        else:
            merged.append((current_start, current_end))
            current_start, current_end = start, end

    merged.append((current_start, current_end))  # add last range

    # Sum number of values
    count = sum(end - start + 1 for start, end in merged)
    print(count)


if __name__ == "__main__":
    main()
