import utils


def get_hash(step: str) -> int:
    result = 0
    for char in step:
        result = ((result + ord(char)) * 17) % 256
    return result


def part_a():
    text = utils.get_lines(15)[0]
    steps = text.split(",")
    result = 0
    for step in steps:
        result += get_hash(step)
    return result


def part_b():
    text = utils.get_lines(15)[0]
    steps = text.split(",")
    # Python dicts are insertion-ordered since 3.7
    boxes: list[dict[str, int]] = [{} for _ in range(256)]
    for step in steps:
        label = step.split("=")[0].split("-")[0]
        box_idx = get_hash(label)
        if "=" in step:
            focal_length = int(step[-1])
            boxes[box_idx][label] = focal_length
        else:
            boxes[box_idx].pop(label, None)

    result = 0
    for box_idx, box in enumerate(boxes):
        for (lens_idx, (label, focal_length)) in enumerate(box.items()):
            this_value = (box_idx + 1) * (lens_idx + 1) * focal_length
            result += this_value
    return result


print(part_b())
