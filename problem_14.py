# noqa: E202
from typing import Any
import utils


def part_a():
    lines = utils.get_lines(14)
    grid = [[char for char in line] for line in lines]
    num_rows = len(grid)

    def locs(char: str) -> list[tuple[int, int]]:
        return [
            (row, col) for row, line in enumerate(grid) for col, c in enumerate(line) if c == char
        ]

    boulder_locs = locs("O")
    boulder_loc_rows_by_col = [
        {row for row, col in boulder_locs if col == c} for c in range(len(grid[0]))
    ]
    block_loc_rows_by_col = [
        {row for row, col in locs("#") if col == c} for c in range(len(grid[0]))
    ]

    result = 0

    for boulder_loc in boulder_locs:
        row, col = boulder_loc
        this_col_rows_above = [
            r for r in (boulder_loc_rows_by_col[col] | block_loc_rows_by_col[col]) if r < row
        ]
        if not this_col_rows_above:
            new_row = 0
        else:
            new_row = max(this_col_rows_above) + 1

        result += num_rows - new_row
        boulder_loc_rows_by_col[col].remove(row)
        boulder_loc_rows_by_col[col].add(new_row)

    return result


# print(part_a())

Loc = tuple[int, int]


def part_b():
    lines = utils.get_lines(14)
    grid = [[char for char in line] for line in lines]
    num_rows = len(grid)
    num_cols = len(grid[0])

    def locs(char: str) -> list[tuple[int, int]]:
        return [
            (row, col) for row, line in enumerate(grid) for col, c in enumerate(line) if c == char
        ]

    boulder_locs = locs("O")
    block_locs = set(locs("#"))

    def print_locs(current_boulder_locs: set[Loc]):
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) in current_boulder_locs:
                    print("O", end="")
                elif (row, col) in block_locs:
                    print("#", end="")
                else:
                    print(".", end="")
            print()
        print("-----")

    block_rows_by_col = [
        {row for row, col in locs("#") if col == c} for c in range(len(grid[0]))
    ]
    block_cols_by_row = [{col for row, col in locs("#") if row == r} for r in range(len(grid))]

    boulder_rows_by_col = [
        {row for row, col in boulder_locs if col == c} for c in range(len(grid[0]))
    ]
    boulder_cols_by_row = [
        {col for row, col in boulder_locs if row == r} for r in range(len(grid))
    ]

    def update_positions(old_row: int, old_col: int, new_row: int, new_col: int) -> list[tuple[int, int]]:
        boulder_rows_by_col[old_col].remove(old_row)
        boulder_rows_by_col[new_col].add(new_row)
        boulder_cols_by_row[old_row].remove(old_col)
        boulder_cols_by_row[new_row].add(new_col)

    def get_boulder_locs() -> list[Loc]:
        return [
            (row, col) for row, cols in enumerate(boulder_cols_by_row) for col in cols
        ]

    seen_positions: dict[tuple[Loc], int] = {}
    boulder_locs = sorted(get_boulder_locs(), key=lambda loc: loc[0])

    for i in range(50):
        if tuple(boulder_locs) in seen_positions:
            old_i = seen_positions[tuple(boulder_locs)]
            print(f"Seen before!, {i} and {old_i}")
            # break
        seen_positions[tuple(boulder_locs)] = i
        # North
        for boulder_loc in boulder_locs:
            row, col = boulder_loc
            this_col_rows_above = [
                r for r in (boulder_rows_by_col[col] | block_rows_by_col[col]) if r < row
            ] + [-1]
            new_row = max(this_col_rows_above) + 1
            update_positions(row, col, new_row, col)
        boulder_locs = get_boulder_locs()
        boulder_locs.sort(key=lambda loc: loc[1])
        # West
        for boulder_loc in boulder_locs:
            row, col = boulder_loc
            this_row_cols_left = [
                c for c in (boulder_cols_by_row[row] | block_cols_by_row[row]) if c < col
            ] + [-1]
            new_col = max(this_row_cols_left) + 1
            update_positions(row, col, row, new_col)
        boulder_locs = get_boulder_locs()
        boulder_locs.sort(key=lambda loc: -loc[0])
        # South
        for boulder_loc in boulder_locs:
            row, col = boulder_loc
            this_col_rows_below = [
                r for r in (boulder_rows_by_col[col] | block_rows_by_col[col]) if r > row
            ] + [num_rows]
            new_row = min(this_col_rows_below) - 1
            update_positions(row, col, new_row, col)
        boulder_locs = get_boulder_locs()
        boulder_locs.sort(key=lambda loc: -loc[1])
        # East
        for boulder_loc in boulder_locs:
            row, col = boulder_loc
            this_row_cols_right = [
                c for c in (boulder_cols_by_row[row] | block_cols_by_row[row]) if c > col
            ] + [num_cols]
            new_col = min(this_row_cols_right) - 1
            update_positions(row, col, row, new_col)
        boulder_locs = get_boulder_locs()
        boulder_locs.sort(key=lambda loc: loc[0])

    print(seen_positions.values())
    final_boulder_locs = next(pos for pos, idx in seen_positions.items() if idx == 43)
    result = sum(
        (num_rows - row_index)
        for row_index, _ in final_boulder_locs
    )
    return result


print(part_b())
