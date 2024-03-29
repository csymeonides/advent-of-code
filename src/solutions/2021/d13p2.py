from utils import run, ParsingConfig, Example

example_answer = None

example_data = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


parsing_config = ParsingConfig(
    field_separator=",",
    single_field=True,
    multi_line=True,
)


def solve(data):
    points = set()
    for d in data[0]:
        x, y = [int(val) for val in d.split(",")]
        points.add((x, y))

    for f in data[1]:
        fold = f.split()[-1].split("=")
        axis = 0 if fold[0] == "x" else 1
        index = int(fold[1])
        for point in points.copy():
            if point[axis] > index:
                points.remove(point)
                new_point = [p for p in point]
                new_point[axis] = 2*index - new_point[axis]
                points.add(tuple(new_point))

    for y in range(max(p[1] for p in points) + 1):
        for x in range(max(p[0] for p in points) + 1):
            char = "#" if (x, y) in points else "."
            print(char, end="")
        print()

    return len(points)


real_answer = "HGAJBEHC"


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
