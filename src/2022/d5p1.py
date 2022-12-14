from src.utils import run, ParsingConfig

example_answer = "CMZ"

example_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class Crane:
    def __init__(self):
        self.state = None

    def parse(self, record):
        if self.state is None:
            n_stacks = int(record[-1].split()[-1])
            self.state = [[] for _ in range(n_stacks)]
            for line in record[:-1]:
                for i in range(n_stacks):
                    value = line[i*4 + 1]
                    if value != " ":
                        self.state[i].append(value)
        else:
            for line in record:
                segments = line.split()
                n_crates = int(segments[1])
                source_stack = int(segments[3]) - 1
                dest_stack = int(segments[5]) - 1
                for _ in range(int(n_crates)):
                    value = self.state[source_stack].pop(0)
                    self.state[dest_stack].insert(0, value)


parsing_config = ParsingConfig(
    parser_class=Crane,
    single_field=True,
    multi_line=True,
    strip=False,
)


def solve(crane: Crane):
    return "".join(stack[0] for stack in crane.state)


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
