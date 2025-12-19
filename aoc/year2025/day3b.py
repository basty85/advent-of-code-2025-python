from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day3.txt"


def read_input() -> list[str]:
    """Read and parse the input file into a list of int."""
    with open(INPUT_FILE) as f:
        return [line.strip() for line in f.readlines()]


def find_highest_k_digit_number(s: str, k: int = 12) -> int | None:
    n = len(s)
    if n < k:
        return None

    result = []
    start = 0

    for pos in range(k):
        # How far can we search?
        end = n - (k - pos - 1)

        max_digit = -1
        max_index = -1

        for i in range(start, end):
            d = int(s[i])
            if d > max_digit:
                max_digit = d
                max_index = i
                if d == 9:
                    break  # best possible value found

        result.append(str(max_digit))
        start = max_index + 1

    return int("".join(result))


def calc_max_joltage(full_list: list[str]) -> list[int]:
    max_per_bank = []
    for str in full_list:
        max_per_bank.append(find_highest_k_digit_number(str))
    return max_per_bank


def main() -> None:
    input = read_input()
    max_per_bank = calc_max_joltage(input)
    total = sum(max_per_bank)
    print(f"max joltage: {total}")


if __name__ == "__main__":
    main()
