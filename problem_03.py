from collections import defaultdict
from dataclasses import dataclass
import utils

Loc = tuple[int, int]


@dataclass
class NumLoc:
    start_loc: Loc
    length: int

    def get_neighbours(self) -> list[Loc]:
        start_row = self.start_loc[0] - 1
        start_col = self.start_loc[1] - 1
        neighbours = []
        for row in (start_row, start_row + 1, start_row + 2):
            for i in range(self.length + 2):
                col = start_col + i
                neighbours.append((row, col))
        return neighbours


def get_lines():
    lines = utils.get_lines(3)
    lines = [f".{line}." for line in lines]
    lines.append("." * len(lines[0]))
    lines.insert(0, "." * len(lines[0]))
    return lines


def get_symbol_locs(lines: list[str]) -> set[Loc]:
    symbol_locs: set[Loc] = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if not char.isdigit() and char != ".":
                symbol_locs.add((row, col))
    return symbol_locs


def get_num_locs(lines: list[str]) -> list[NumLoc]:
    num_locs: list[tuple[int, NumLoc]] = []
    for row, line in enumerate(lines):
        line += "."
        digits = []
        start_col = None
        for col, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
                if start_col is None:
                    start_col = col
            elif digits:
                final_num = int("".join(digits))
                num_loc = NumLoc(start_loc=(row, start_col), length=len(digits))
                num_locs.append((final_num, num_loc))
                digits = []
                start_col = None
    return num_locs


def part_a():
    lines = get_lines()
    symbol_locs = get_symbol_locs(lines)
    num_locs: list[tuple[int, NumLoc]] = get_num_locs(lines)

    result = 0
    for num, num_loc in num_locs:
        neighbours = num_loc.get_neighbours()
        if any(neighbour in symbol_locs for neighbour in neighbours):
            result += num
    return result


print(part_a())


def part_b():
    lines = get_lines()
    num_locs: list[tuple[int, NumLoc]] = get_num_locs(lines)

    result = 0
    star_nums = defaultdict(list)
    for num, num_loc in num_locs:
        neighbours = num_loc.get_neighbours()
        for neighbour in neighbours:
            if lines[neighbour[0]][neighbour[1]] == "*":
                star_nums[neighbour].append(num)
    for symbol_loc, nums in star_nums.items():
        if len(nums) == 2:
            result += (nums[0] * nums[1])
    return result


print(part_b())
