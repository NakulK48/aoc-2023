from dataclasses import dataclass
from typing import Any
import utils


def get_mirror_index(iterable: list[str]) -> int | None:
    for mirror_idx in range(1, len(iterable)):
        distance = min(mirror_idx, len(iterable) - mirror_idx)
        to_left = iterable[(mirror_idx - distance) : mirror_idx][::-1]
        to_right = iterable[mirror_idx : mirror_idx + distance]
        if to_left == to_right:
            return mirror_idx
    return None


def part_a():
    sections = utils.get_sections(13)
    result = 0
    for section in sections:
        rows = section.splitlines()
        columns = ["".join([row[i] for row in rows]) for i in range(len(rows[0]))]
        row_mirror_idx = get_mirror_index(rows)
        if row_mirror_idx:
            result += 100 * row_mirror_idx
        else:
            result += get_mirror_index(columns)
    return result


print(part_a())


def single_mismatched_index(iter1: list[Any], iter2: list[Any]) -> int | None:
    mismatches = [i for i, (a, b) in enumerate(zip(iter1, iter2)) if a != b]
    if len(mismatches) == 1:
        return mismatches[0]
    return None


def get_mirror_index_b(iterable: list[str]) -> int | None:
    for mirror_idx in range(1, len(iterable)):
        distance = min(mirror_idx, len(iterable) - mirror_idx)
        to_left = iterable[(mirror_idx - distance):mirror_idx][::-1]
        to_right = iterable[mirror_idx:mirror_idx + distance]
        mismatched_iterable_index = single_mismatched_index(to_left, to_right)
        if mismatched_iterable_index is None:
            continue
        mismatched_cell_index = single_mismatched_index(
            to_left[mismatched_iterable_index], to_right[mismatched_iterable_index]
        )
        if mismatched_cell_index is not None:
            return mirror_idx

    return None


def part_b():
    sections = utils.get_sections(13)
    result = 0
    for section in sections:
        rows = section.splitlines()
        columns = ["".join([row[i] for row in rows]) for i in range(len(rows[0]))]
        row_mirror_idx = get_mirror_index_b(rows)
        if row_mirror_idx:
            result += 100 * row_mirror_idx
        else:
            result += get_mirror_index_b(columns)
    return result


print(part_b())
