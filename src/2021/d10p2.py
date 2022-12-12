from src.utils import run, ParsingConfig

example_answer = 288957

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
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

symbols = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def get_score(row):
    stack = []
    score = 0
    for d in row:
        if d in symbols:
            stack.append(d)
        elif stack:
            expected = symbols[stack.pop()]
            if d != expected:
                return None
    while stack:
        closer = symbols[stack.pop()]
        score = (score * 5) + points[closer]
    return score


def solve(data):
    scores = [get_score(row) for row in data]
    sorted_scores = sorted([s for s in scores if s is not None])
    return sorted_scores[len(sorted_scores) // 2]


real_answer = 2360030859


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
