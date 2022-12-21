from utils import run, ParsingConfig

example_answer = 56000011

example_data = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def parse(*line):
    sensor_x = int(line[2].split("=")[-1].replace(",", ""))
    sensor_y = int(line[3].split("=")[-1].replace(":", ""))
    beacon_x = int(line[8].split("=")[-1].replace(",", ""))
    beacon_y = int(line[9].split("=")[-1].replace(":", ""))
    distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
    return (sensor_x, sensor_y), (beacon_x, beacon_y), distance


parsing_config = ParsingConfig(
    parser_func=parse,
)


def add(ranges, range_to_add):
    add_start, add_end = range_to_add
    for i in range(len(ranges)):
        start, end = ranges[i]
        if add_start < start:
            if add_end + 1 < start:
                ranges.insert(i, range_to_add)
            else:
                new_end = max(end, add_end)
                ranges[i] = (add_start, new_end)
                if i+1 < len(ranges):
                    next_start, next_end = ranges[i+1]
                    if next_start <= new_end + 1:
                        ranges[i] = (add_start, max(new_end, next_end))
                        ranges.pop(i+1)
            return
        elif add_start <= end + 1 or add_end <= end + 1:
            new_end = max(end, add_end)
            ranges[i] = (start, new_end)
            if i+1 < len(ranges):
                next_start, next_end = ranges[i+1]
                if next_start <= new_end + 1:
                    ranges[i] = (start, max(new_end, next_end))
                    ranges.pop(i+1)
            return
    ranges.append(range_to_add)


def find_target_x(not_here, max_value):
    if not_here:
        if not_here[0][0] == 1 and not_here[0][1] >= max_value:
            return 0
        elif not_here[0][0] <= 0 and not_here[0][1] == max_value - 1:
            return max_value
        elif len(not_here) > 1 and not_here[0][0] <= 0 and not_here[1][1] >= max_value:
            candidate = None
            for i in range(len(not_here) - 1):
                if not_here[i][1] + 2 == not_here[i+1][0]:
                    if candidate:
                        return None
                    candidate = not_here[i][1] + 1
            if candidate:
                return candidate
    return None


def try_target_y(data, target_y, max_value):
    not_here = []

    for (sensor_x, sensor_y), (beacon_x, beacon_y), distance in data:
        if beacon_y == target_y:
            add(not_here, (beacon_x, beacon_x))

        target_distance = abs(target_y - sensor_y)
        x_range = distance - target_distance
        if x_range >= 0:
            add(not_here, (sensor_x - x_range, sensor_x + x_range))

        if not_here and not_here[0][0] <= 0 and not_here[0][1] >= max_value:
            return None

    target_x = find_target_x(not_here, max_value)
    if target_x is not None:
        return (target_x * 4000000) + target_y


def solve(data):
    max_value = 20 if len(data) == 14 else 4000000

    for target_y in range(max_value + 1):
        if target_y % 100000 == 0:
            print(target_y)

        result = try_target_y(data, target_y, max_value)
        if result is not None:
            return result

    raise ValueError("No solution found!")


real_answer = 10884459367718


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
