import utils


def get_overlap(nums_str: str) -> int:
    win_str, have_str = nums_str.split(" | ")
    wins = set(win_str.strip().split())
    have = set(have_str.strip().split())
    return len(wins & have)


def part_a():
    lines = utils.get_lines(4)
    result = 0
    for line in lines:
        nums_str = line[line.find(":") + 1:]
        overlap = get_overlap(nums_str)
        if overlap > 0:
            result += 2**(overlap - 1)
    return result


# print(part_a())


def part_b():
    lines = utils.get_lines(4)
    cards_by_card = {}

    def cards_from_card(base: int):
        if base in cards_by_card:
            return cards_by_card[base]
        _, nums_str = lines[base - 1].split(": ")
        overlap = get_overlap(nums_str)
        result = 1  # current card
        for i in range(overlap):
            result += cards_from_card(base + i + 1)
        cards_by_card[base] = result
        return result

    final_result = 0
    for i in range(len(lines)):
        final_result += cards_from_card(i + 1)
    return final_result


print(part_b())
