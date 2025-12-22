from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day6.txt"


def read_input() -> tuple[list[int], list[str]]:
    with open(INPUT_FILE) as f:
        lines = [line.strip() for line in f if line.strip()]

    output_numbers_str = []
    output_numbers = 0
    numbers = lines[:-1]

    for col in range(len(numbers[0])):
        new_number = ""
        for row in numbers:
            new_number += row[col]
        output_numbers_str.append(new_number)

    output_numbers = [int(x.strip()) if x.strip() else 0 for x in output_numbers_str]

    operator_line = lines[-1]
    operators = operator_line.split()

    return output_numbers, operators


def main() -> None:
    numbers, operators = read_input()
    it = 0
    results = []

    if operators[it] == "+":
        total = 0
    else:
        total = 1

    for number in numbers:
        if number == 0:
            results.append(total)
            it += 1
            if operators[it] == "+":
                total = 0
            else:
                total = 1
        else:
            if operators[it] == "+":
                total += number
            else:
                total *= number
    results.append(
        total
    )  # Append last total value because there is no more "zero" case
    print(sum(results))


if __name__ == "__main__":
    main()
