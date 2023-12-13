from functools import cache
import itertools
import utils


def get_group_lengths(line: str) -> list[int]:
    groups: list[int] = []
    run_length = 0
    for char in line:
        if char == "#":
            run_length += 1
        elif char == ".":
            if run_length:
                groups.append(run_length)
            run_length = 0
    if run_length:
        groups.append(run_length)
    return groups


def get_sub_lines(line_with_wildcards: str, num_broken_total: int) -> list[str]:
    question_indices = [i for i, char in enumerate(line_with_wildcards) if char == "?"]
    num_broken_known = sum(char == "#" for char in line_with_wildcards)
    num_broken_unknown = num_broken_total - num_broken_known
    all_indexes_to_change = itertools.combinations(question_indices, num_broken_unknown)
    sub_lines = []
    for indexes_to_change in all_indexes_to_change:
        sub_line = list(line_with_wildcards)
        for index in indexes_to_change:
            sub_line[index] = "#"
        sub_lines.append("".join(sub_line).replace("?", "."))

    return sub_lines


def get_combination_count_a(full_line_with_wildcards: str) -> int:
    line_with_wildcards, counts_str = full_line_with_wildcards.split()
    counts = [int(count) for count in counts_str.split(",")]
    num_broken = sum(counts)
    sub_lines = get_sub_lines(line_with_wildcards, num_broken)
    result = sum(1 for sub_line in sub_lines if get_group_lengths(sub_line) == counts)
    return result


@cache
def number_of_ways(remaining_line: str, current_run: int, remaining_counts: tuple[int]):
    if not remaining_counts:
        return 0 if "#" in remaining_line else 1
    if current_run > remaining_counts[0]:
        return 0
    if not remaining_line:
        return 1 if remaining_counts == (current_run,) else 0

    if remaining_line[0] == "#":
        return number_of_ways(remaining_line[1:], current_run + 1, remaining_counts)
    if remaining_line[0] == ".":
        if current_run == 0:
            ways_with_dot = number_of_ways(remaining_line[1:], 0, remaining_counts)
        elif current_run == remaining_counts[0]:
            ways_with_dot = number_of_ways(remaining_line[1:], 0, remaining_counts[1:])
        else:
            ways_with_dot = 0
        return ways_with_dot
    if remaining_line[0] == "?":
        ways_with_hash = number_of_ways(remaining_line[1:], current_run + 1, remaining_counts)
        if current_run == 0:
            ways_with_dot = number_of_ways(remaining_line[1:], 0, remaining_counts)
        elif current_run == remaining_counts[0]:
            ways_with_dot = number_of_ways(remaining_line[1:], 0, remaining_counts[1:])
        else:
            ways_with_dot = 0

        return ways_with_hash + ways_with_dot

    raise ValueError(f"Unexpected character {remaining_line[0]}")


def get_combination_count_b(full_line_with_wildcards: str) -> int:
    base_line_with_wildcards, base_counts_str = full_line_with_wildcards.split()
    line_with_wildcards = "?".join([base_line_with_wildcards] * 5)
    counts = [int(count) for count in base_counts_str.split(",")] * 5
    result = number_of_ways(line_with_wildcards, 0, tuple(counts))
    return result


def part_a():
    lines = utils.get_lines(12)
    result = sum(get_combination_count_a(line) for line in lines)
    return result


print(part_a())


def part_b():
    lines = utils.get_lines(12)
    result = sum(get_combination_count_b(line) for line in lines)
    return result


print(part_b())
