from src.utils import run, ParsingConfig

example_answer = 2188189693529

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
    initial_state = data[0][0]
    mappings = {pair: insert for [pair, insert] in data[1:]}
    state = {pair: 0 for pair in mappings}
    for i in range(len(initial_state) - 1):
        state[initial_state[i:i + 2]] += 1

    for _ in range(40):
        new_state = {pair: 0 for pair in mappings}
        for pair, count in state.items():
            if count > 0:
                insert = mappings[pair]
                new_state[pair[0] + insert] += count
                new_state[insert + pair[1]] += count
        state = new_state

    counts = {pair[0]: sum(val for p, val in state.items() if p[0] == pair[0]) for pair in state}
    counts[initial_state[-1]] += 1
    return max(counts.values()) - min(counts.values())


real_answer = None


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
