import utils


Loc = tuple[int, int]


def part_a():
    lines = utils.get_lines(11)
    grid = [
        [char for char in line]
        for line in lines
    ]
    row = 0
    while row < len(grid):
        line = grid[row]
        if all(char == "." for char in line):
            grid.insert(row + 1, ["."] * len(line))
            row += 2
        else:
            row += 1

    col = 0
    while col < len(grid[0]):
        line = [grid[row][col] for row in range(len(grid))]
        if all(char == "." for char in line):
            for row in range(len(grid)):
                grid[row].insert(col + 1, ".")
            col += 2
        else:
            col += 1

    galaxies: list[Loc] = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                galaxies.append((row, col))

    result = 0

    for row1, col1 in galaxies:
        for row2, col2 in galaxies:
            distance = abs(row1 - row2) + abs(col1 - col2)
            result += distance
    return result // 2  # we count each pair twice


print(part_a())


def part_b():
    lines = utils.get_lines(11)

    grid = [
        [char for char in line]
        for line in lines
    ]

    galaxies: list[Loc] = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                galaxies.append((row, col))

    expanded_rows: set[int] = set()
    expanded_cols: set[int] = set()

    for row, line in enumerate(grid):
        if all(char == "." for char in line):
            expanded_rows.add(row)
    for col in range(len(grid[0])):
        line = [grid[row][col] for row in range(len(grid))]
        if all(char == "." for char in line):
            expanded_cols.add(col)

    expansion_factor = 1_000_000
    result = 0
    for row1, col1 in galaxies:
        for row2, col2 in galaxies:
            distance = 0
            min_row = min(row1, row2)
            max_row = max(row1, row2)
            min_col = min(col1, col2)
            max_col = max(col1, col2)
            for rowi in range(min_row, max_row):
                if rowi in expanded_rows:
                    distance += expansion_factor
                else:
                    distance += 1
            for coli in range(min_col, max_col):
                if coli in expanded_cols:
                    distance += expansion_factor
                else:
                    distance += 1
            result += distance
    return result // 2  # we count each pair twice


print(part_b())
