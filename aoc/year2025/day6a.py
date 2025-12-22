from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day6.txt"


def read_input() -> tuple[list[list[int]], list[str]]:
    """Read input: numeric matrix + operator list from last line."""
    with open(INPUT_FILE) as f:
        lines = [line.strip() for line in f if line.strip()]

    *number_lines, operator_line = lines

    numbers = [[int(x) for x in line.split()] for line in number_lines]

    operators = operator_line.split()

    return numbers, operators


def main() -> None:
    numbers, operators = read_input()

    result = 0

    # Iterator over columns
    for col_idx, op in enumerate(operators):
        # first column idx = 0 etc.
        column_values = [row[col_idx] for row in numbers]

        # Start value dependent of operator
        if op == "*":
            total = 1
        else:
            total = 0

        # Actual calc
        for val in column_values:
            if op == "+":
                total += val
            elif op == "*":
                total *= val
            else:
                raise ValueError(f"Unbekannter Operator: {op}")

        # Calc grand total
        result += total

    print(result)


if __name__ == "__main__":
    main()
