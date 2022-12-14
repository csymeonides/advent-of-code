from utils import run, ParsingConfig

example_answer = 10

example_data = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""


parsing_config = ParsingConfig(
    field_separator="-",
)


def solve(data):
    edges = {}
    for edge in data:
        edges.setdefault(edge[0], set()).add(edge[1])
        edges.setdefault(edge[1], set()).add(edge[0])

    paths = []
    draft_paths = [["start"]]
    while draft_paths:
        path = draft_paths.pop()
        for dest in edges[path[-1]]:
            if dest not in path or dest.upper() == dest:
                new_path = path + [dest]
                if dest == "end":
                    paths.append(new_path)
                else:
                    draft_paths.append(new_path)
    return len(paths)


real_answer = 4413


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
