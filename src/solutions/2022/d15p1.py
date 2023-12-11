from utils import run, ParsingConfig, Example

example_answer = 26

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
    return (sensor_x, sensor_y), (beacon_x, beacon_y)


parsing_config = ParsingConfig(
    parser_func=parse,
)


def solve(data):
    target_y = 10 if len(data) == 14 else 2000000  # example vs real data
    not_here = set()

    for (sensor_x, sensor_y), (beacon_x, beacon_y) in data:
        distance = abs(beacon_x - sensor_x) + abs(beacon_y - sensor_y)
        target_distance = abs(target_y - sensor_y)
        x_range = distance - target_distance
        if x_range >= 0:
            for i in range(x_range + 1):
                not_here.add(sensor_x + i)
                not_here.add(sensor_x - i)

    for _, (beacon_x, beacon_y) in data:
        if beacon_y == target_y:
            not_here.discard(beacon_x)

    return len(not_here)


real_answer = 5142231


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
