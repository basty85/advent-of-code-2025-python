from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day2.txt"


def read_input() -> list[tuple[int, int]]:
    """Read and parse the input file into a list of (start, end) tuples."""
    with open(INPUT_FILE) as f:
        data = f.read().strip()
        ranges = []
        for item in data.split(","):
            start, end = item.split("-")
            ranges.append((int(start), int(end)))
        return ranges


def generate_ids_to_check(input: list[tuple[int, int]]) -> list[int]:
    all_relevant_ids = []
    for start_id, stop_id in input:
        current_id = start_id
        while current_id <= stop_id:
            all_relevant_ids.append(current_id)
            current_id += 1
    return all_relevant_ids


def is_invalid_id(n: int) -> bool:
    s = str(n)
    length = len(s)

    for block_len in range(1, length // 2 + 1):
        if length % block_len != 0:
            continue

        block = s[:block_len]
        if block * (length // block_len) == s:
            return True

    return False


def process_ids(all_relevant_ids: list[int]) -> list[int]:
    invalid_ids = []
    for id in all_relevant_ids:
        if is_invalid_id(id):
            invalid_ids.append(id)
    return invalid_ids


def main() -> None:
    input = read_input()
    all_relevant_ids = generate_ids_to_check(input)
    invalid_ids = process_ids(all_relevant_ids)
    sum_invalid_ids = sum(invalid_ids)
    print(f"Sum invalid ids is: {sum_invalid_ids}")


if __name__ == "__main__":
    main()
