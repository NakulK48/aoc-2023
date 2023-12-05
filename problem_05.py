from dataclasses import dataclass
import itertools
import time
import utils


@dataclass
class MapOffset:
    start: int
    end: int
    offset: int


@dataclass
class SingleMap:
    offsets: list[MapOffset]

    def map_value(self, value: int) -> int:
        for offset in self.offsets:
            if offset.start <= value < offset.end:
                return value + offset.offset
        return value

    def map_reverse(self, value: int) -> int:
        for offset in self.offsets:
            new_start = offset.start + offset.offset
            new_end = offset.end + offset.offset
            if new_start <= value < new_end:
                return value - offset.offset
        return value

    @staticmethod
    def from_section(section: str) -> "SingleMap":
        lines = section.strip().splitlines()[1:]
        current_map = SingleMap([])
        for line in lines:
            dest_start, source_start, length = [int(x) for x in line.split()]
            current_map.offsets.append(
                MapOffset(source_start, source_start + length, dest_start - source_start)
            )
        return current_map


def get_maps(sections: list[str]) -> list[SingleMap]:
    maps: list[SingleMap] = []
    for section in sections[1:]:
        current_map = SingleMap.from_section(section)
        maps.append(current_map)
    return maps


def part_a():
    sections = utils.get_sections(5)
    seeds = [int(x) for x in sections[0].strip().split(": ")[1].split()]
    maps = get_maps(sections)
    location_number = float("inf")
    for seed in seeds:
        current = seed
        for single_map in maps:
            current = single_map.map_value(current)
        location_number = min(location_number, current)
    return location_number


print(part_a())


@dataclass
class Range:
    start: int
    length: int

    def __contains__(self, item: int) -> bool:
        return self.start <= item < (self.start + self.length)


def part_b():
    sections = utils.get_sections(5)
    seeds_and_offsets = [int(x) for x in sections[0].strip().split(": ")[1].split()]
    seeds = seeds_and_offsets[::2]
    offsets = seeds_and_offsets[1::2]

    ranges = [Range(seed, offset) for seed, offset in zip(seeds, offsets)]
    maps = get_maps(sections)
    maps_backwards = maps[::-1]
    for result in itertools.count(start=0):
        if (result % 1_000_000) == 0:
            print(result)
        current = result
        for single_map in maps_backwards:
            current = single_map.map_reverse(current)
        if any(current in some_range for some_range in ranges):
            return result


print(part_b())
