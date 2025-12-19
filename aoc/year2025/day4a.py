from pathlib import Path

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day4.txt"
STARTING_POSITION = 50


def read_binary_matrix() -> list[list[int]]:
    with open(INPUT_FILE, "r") as f:
        return [
            [1 if c == "@" else 0 for c in line.rstrip("\n")]
            for line in f
            if line.strip()
        ]


def mark_accessible(grid: list[list[int]]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    result = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Sum of 8 neighbors
                neighbor_sum = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            neighbor_sum += grid[nr][nc]
                if neighbor_sum < 4:
                    result[r][c] = 1  # reachable
    return result


def main() -> None:
    input_as_int = read_binary_matrix()
    result = mark_accessible(input_as_int)
    count = sum(sum(row) for row in result)

    print(f"Max reachable rolls: {count}")


if __name__ == "__main__":
    main()
