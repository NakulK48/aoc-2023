import itertools
import math
from typing import TypedDict
import utils


class Node(TypedDict):
    L: str
    R: str


def get_nodes(all_lines: list[str]) -> dict[str, Node]:
    nodes: dict[str, Node] = {}
    for line in all_lines[2:]:
        this_node, next_nodes_str = line.split(" = ")
        left_node, right_node = next_nodes_str.strip("()").split(", ")
        nodes[this_node] = Node(L=left_node, R=right_node)
    return nodes


def part_a() -> int:
    lines = utils.get_lines(8)
    directions = lines[0]
    nodes = get_nodes(lines)

    current = "AAA"
    steps = 0
    for direction in itertools.cycle(directions):
        if current == "ZZZ":
            return steps
        current = nodes[current][direction]
        steps += 1
    return steps


# print(part_a())


def part_b() -> int:
    lines = utils.get_lines(8)
    directions = lines[0]
    nodes = get_nodes(lines)

    currents: list[str] = [name for name in nodes if name.endswith("A")]
    steps = 0
    z_intervals = [None] * 6
    for direction in itertools.cycle(directions):
        for idx, current in enumerate(currents):
            if current.endswith("Z") and z_intervals[idx] is None:
                z_intervals[idx] = steps
        if all(z_intervals):
            return math.lcm(*z_intervals)
        new_currents: list[str] = []
        for current in currents:
            new_currents.append(nodes[current][direction])
        currents = new_currents
        steps += 1


print(part_b())
