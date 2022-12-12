from src.utils import run, ParsingConfig

example_answer = 26397

example_data = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


parsing_config = ParsingConfig(
    single_field=True,
)

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def solve(data):
    total = 0
    for row in data:
        stack = []
        for d in row:
            if d in symbols:
                stack.append(d)
            elif stack:
                expected = symbols[stack.pop()]
                if d != expected:
                    total += points[d]
                    break
    return total


real_answer = 321237


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
