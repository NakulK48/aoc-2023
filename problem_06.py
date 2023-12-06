import utils


def part_a():
    lines = utils.get_lines(6)
    times = [int(x) for x in lines[0].split()[1:]]
    distances = [int(x) for x in lines[1].split()[1:]]
    result = 1
    for time, min_distance in zip(times, distances):
        num_ways = 0
        for hold_time in range(time):
            distance = (time - hold_time) * hold_time
            if distance > min_distance:
                num_ways += 1
        result *= num_ways
    return result


print(part_a())


def part_b():
    lines = utils.get_lines(6)
    time = int("".join(lines[0].split()[1:]))
    min_distance = int("".join(lines[1].split()[1:]))
    num_ways = 0
    for hold_time in range(time):
        distance = (time - hold_time) * hold_time
        if distance > min_distance:
            num_ways += 1
        elif num_ways > 0:  # the distance will only get lower from here
            break
    return num_ways


print(part_b())
