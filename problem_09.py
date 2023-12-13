import utils


def part_a():
    lines = utils.get_lines(9)
    result = 0
    for line in lines:
        base_nums = [int(num) for num in line.split()]
        final_nums = [base_nums[-1]]
        current = base_nums
        while any(current):  # not all zero
            current = [
                current[i] - current[i-1] for i in range(1, len(current))
            ]
            final_nums.append(current[-1])
        final_nums.reverse()
        for i in range(2, len(final_nums)):
            final_nums[i] = final_nums[i] + final_nums[i-1]
        result += final_nums[-1]
    return result


# print(part_a())


def part_b():
    lines = utils.get_lines(9)
    result = 0
    for line in lines:
        base_nums = [int(num) for num in line.split()]
        first_nums = [base_nums[0]]
        current = base_nums
        while any(current):  # not all zero
            current = [
                current[i] - current[i-1] for i in range(1, len(current))
            ]
            first_nums.append(current[0])
        first_nums.reverse()
        for i in range(2, len(first_nums)):
            first_nums[i] = first_nums[i] - first_nums[i-1]
        result += first_nums[-1]
    return result


print(part_b())
