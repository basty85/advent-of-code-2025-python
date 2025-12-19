from pathlib import Path
import numpy as np
from scipy.signal import convolve2d

INPUT_FILE = Path(__file__).parent.parent.parent / "inputs" / "2025" / "day4.txt"


def read_binary_matrix() -> np.ndarray:
    """Liest die Datei ein und konvertiert sie in eine 0/1 NumPy-Matrix"""
    with open(INPUT_FILE, "r") as f:
        grid = [
            [1 if c == "@" else 0 for c in line.rstrip("\n")]
            for line in f
            if line.strip()
        ]
    return np.array(grid, dtype=int)


def mark_accessible(grid: np.ndarray) -> np.ndarray:
    """Marks reachable rolls in the matrix"""
    # Kernel for 8 neighbors
    kernel = np.ones((3, 3), dtype=int)
    kernel[1, 1] = 0

    neighbor_sum = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)
    accessible = (grid == 1) & (neighbor_sum < 4)
    return accessible.astype(int)


def main() -> None:
    grid = read_binary_matrix()
    total_reachable = 0

    while True:
        reachable = mark_accessible(grid)
        n_reached = reachable.sum()
        if n_reached == 0:
            break  # nothing more reachable -> finish
        total_reachable += n_reached
        grid = grid - reachable  # remove reached rolls

    print(f"Max reachable rolls: {total_reachable}")


if __name__ == "__main__":
    main()
