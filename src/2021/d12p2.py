from src.utils import run, ParsingConfig

example_answer = 36

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
    # parser_class=None,
    # parser_func=lambda *args: tuple(args),
    field_separator="-",
    # value_converter=int,
    # single_field=True,
    # multi_line=True,
    # strip=False,
)


def is_valid(dest, path):
    if dest not in path or dest.upper() == dest:
        return True
    small = [p for p in path if p.lower() == p]
    return len(small) == len(set(small))


def solve(data):
    edges = {}
    for edge in data:
        if edge[1] != "start":
            edges.setdefault(edge[0], set()).add(edge[1])
        if edge[0] != "start":
            edges.setdefault(edge[1], set()).add(edge[0])

    paths = []
    draft_paths = [["start"]]
    while draft_paths:
        path = draft_paths.pop()
        for dest in edges[path[-1]]:
            if is_valid(dest, path):
                new_path = path + [dest]
                if dest == "end":
                    paths.append(new_path)
                else:
                    draft_paths.append(new_path)
    return len(paths)


real_answer = 118803


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
