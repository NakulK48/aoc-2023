import utils


def part_a() -> int:
    lines = utils.get_lines(1)
    result = 0
    for line in lines:
        digits = [d for d in line if d.isdigit()]
        num = int(f"{digits[0]}{digits[-1]}")
        result += num
    return result


# print(part_a())

DIGIT_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def process_line(line: str) -> list[int]:
    digits: list[int] = []
    for idx, char in enumerate(line):
        if char.isdigit():
            digits.append(int(char))
            continue
        for digit_idx, digit_str in enumerate(DIGIT_STRINGS):
            if line[idx:].startswith(digit_str):
                digits.append(digit_idx + 1)
                break
    return digits


def part_b() -> int:
    lines = utils.get_lines(1)
    result = 0
    for line in lines:
        digits = process_line(line)
        num = int(f"{digits[0]}{digits[-1]}")
        result += num
    return result


print(part_b())
