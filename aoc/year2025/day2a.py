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
            if len(str(current_id)) % 2 == 0:
                all_relevant_ids.append(current_id)
            current_id += 1
    return all_relevant_ids


def find_invalid_ids(input_all_ids: list[int]) -> list[int]:
    invalid_ids = []
    for id in input_all_ids:
        id_str = str(id)
        length = len(id_str)
        half = length // 2
        first_half = id_str[:half]
        second_half = id_str[half:]
        if first_half == second_half:
            invalid_ids.append(id)
    return invalid_ids


def main() -> None:
    input = read_input()
    all_relevant_ids = generate_ids_to_check(input)
    invalid_ids = find_invalid_ids(all_relevant_ids)
    sum_invalid_ids = sum(invalid_ids)
    print(f"Found {len(all_relevant_ids)} IDs with even digit count")
    print(f"Found {len(invalid_ids)} invalid IDs (identical halves)")
    print(f"Sum invalid ids is: {sum_invalid_ids}")


if __name__ == "__main__":
    main()
