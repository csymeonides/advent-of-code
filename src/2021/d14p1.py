from src.utils import run, ParsingConfig

example_answer = 1588

example_data = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


parsing_config = ParsingConfig(
    field_separator=" -> ",
)


def solve(data):
    state = data[0][0]
    mappings = {pair: insert for [pair, insert] in data[1:]}

    for _ in range(10):
        new_state = ""
        for i in range(len(state) - 1):
            insert = mappings[state[i:i+2]]
            new_state += state[i] + insert
        state = new_state + state[-1]

    counts = [state.count(x) for x in set(state)]
    return max(counts) - min(counts)


real_answer = 2768


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
