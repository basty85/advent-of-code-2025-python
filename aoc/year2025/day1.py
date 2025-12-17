from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day1.txt"
STARTING_POSITION = 50


def read_input() -> list[tuple[str, int]]:
    """Read and parse the input file into a list of (direction, steps) tuples."""
    with open(INPUT_FILE) as f:
        return [(line[0], int(line[1:])) for line in f if line.strip()]


def count_zero(moves: list[tuple[str, int]]) -> int:
    """Calculates how often zero is reached after every move"""
    position = STARTING_POSITION
    zero_counts = 0
    for direction, steps in moves:
        if direction == "R":
            position += steps
        else:
            position -= steps

        # Wrap position to stay in range [0, 99]
        position = position % 100

        # Check if we landed on 0 after any move
        if position == 0:
            zero_counts += 1
    return zero_counts


def solve_part2(moves: list[tuple[str, int]]) -> int:
    """Count total times dial points at 0"""
    position = STARTING_POSITION
    zero_count = 0

    for direction, steps in moves:
        old_position = position

        if direction == "R":
            position += steps
        else:
            position -= steps

        if position > 0:
            zero_count += abs(position // 100 - old_position // 100)
        else:
            if position % 100 == 0:  # Correct that // in python rounds down to -inf
                zero_count += 1
            zero_count += abs(position // 100 - old_position // 100)

        # Wenn wir genau auf Null starten, zählt der erste Crossing nicht
        if old_position == 0 and position < 0:
            zero_count -= 1

        # Wrap position to stay in range [0, 99]
        position = position % 100

    return zero_count


def main() -> None:
    moves = read_input()
    part1_result = count_zero(moves)
    print(f"Part 1 result: {part1_result}")

    part2_result = solve_part2(moves)
    print(f"Part 2 result: {part2_result}")


if __name__ == "__main__":
    main()
