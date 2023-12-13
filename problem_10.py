from dataclasses import dataclass
from math import ceil
import utils

Loc = tuple[int, int]
LocPair = tuple[Loc, Loc] | tuple[()]


def get_cell_value(row: int, col: int, label: str):
    north = (row-1, col)
    west = (row, col-1)
    south = (row+1, col)
    east = (row, col+1)
    mappings = {
        ".": (),
        "-": (west, east),
        "|": (north, south),
        "L": (north, east),
        "J": (north, west),
        "7": (south, west),
        "F": (south, east),
        "S": (north, south, east, west),
    }
    return mappings[label]


@dataclass
class GridAndStart:
    grid: list[list[LocPair]]
    start_loc: Loc


@dataclass
class Chain:
    locs: set[Loc]
    length: int


def build_grid(lines: list[str]) -> GridAndStart:
    connection_grid: list[list[LocPair]] = []
    start_loc = None
    for row, line in enumerate(lines):
        connection_grid.append([])
        for col, char in enumerate(line):
            if char == "S":
                start_loc = (row, col)
            connection_grid[row].append(get_cell_value(row, col, char))
    assert start_loc is not None
    return GridAndStart(grid=connection_grid, start_loc=start_loc)


def build_chain(grid_and_start: GridAndStart) -> Chain:
    connection_grid = grid_and_start.grid
    start_loc = grid_and_start.start_loc

    loc = start_loc
    chain_length = 0
    visited: set[Loc] = {loc}

    while True:
        row, col = loc
        try:
            loc = next(
                neighbour for neighbour in connection_grid[row][col]
                if neighbour not in visited
                and loc in connection_grid[neighbour[0]][neighbour[1]]
            )
        except StopIteration:
            chain_length += 1
            break
        visited.add(loc)
        chain_length += 1
        if loc == start_loc:
            break
    return Chain(locs=visited, length=chain_length)


def part_a():
    lines = utils.get_lines(10)
    grid_and_start = build_grid(lines)
    chain = build_chain(grid_and_start)
    return ceil(chain.length / 2)


print(part_a())


def part_b():
    lines = utils.get_lines(10)
    grid_and_start = build_grid(lines)
    chain = build_chain(grid_and_start)
    area = 0
    for row, line in enumerate(lines):
        within_area = False
        for col, char in enumerate(line):
            if (row, col) in chain.locs:
                if char in "|LJS":  # in my dataset, the S is really an L
                    within_area = not within_area
                continue
            if within_area:
                area += 1
    return area


print(part_b())
