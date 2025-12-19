from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day3.txt"


def read_input() -> list[str]:
    """Read and parse the input file into a list of int."""
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f.readlines()]


def find_highest_value_per_bank(input_str: str) -> int:
    """Finds the highest possible value per bank and returns it as an int"""
    for i in range(9, -1, -1):
        pos1 = input_str.find(str(i))
        if pos1 != -1:
            for j in range(9, -1, -1):
                pos2 = input_str.find(str(j), pos1 + 1)
                if pos2 != -1:
                    return int(f"{i}{j}")
    return None  # If no two valid values exist


def calc_max_joltage(full_list: list[str]) -> list[int]:
    max_per_bank = []
    for str in full_list:
        max_per_bank.append(find_highest_value_per_bank(str))
    return max_per_bank


def main() -> None:
    input = read_input()
    max_per_bank = calc_max_joltage(input)
    total = sum(max_per_bank)
    print(f"max joltage: {total}")


if __name__ == "__main__":
    main()
