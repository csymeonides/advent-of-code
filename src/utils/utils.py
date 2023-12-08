import time
from contextlib import contextmanager
from typing import List

from utils.fetcher import get_input_data, check_real_answer
from utils.parser import parse_input


def check(answer_function, input, expected):
    result = answer_function(input)
    assert result == expected, f"Expected {expected} but was {result}"


@contextmanager
def timer(label):
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start_time
        print(f"{label} took {elapsed:.1f}s to solve")


def prepare_example_data(example_data: str) -> List[str]:
    data = example_data.split("\n")
    if data[0] == "":
        data = data[1:]
    if data[-1] == "":
        data = data[:-1]
    return data


def _solve_and_check(solve, label, data, expected, wrong_answers=None):
    with timer(label):
        answer = solve(data)
    if expected is None:
        print(f"Answer: {answer}")
        if wrong_answers and answer in wrong_answers:
            print("(this is wrong, you've tried it before)")
        elif label == "Real":
            check_real_answer(answer)
    else:
        assert expected == answer, f"Expected {expected} but got {answer}"
        print(f"CORRECT! Answer: {answer}")


def run(example_data, example_answer, parsing_config, solve, real_answer=None, wrong_answers=None):
    raw_real_data = get_input_data()

    example_data = parse_input(parsing_config, data=prepare_example_data(example_data))
    _solve_and_check(solve, "Example", example_data, example_answer)

    print()

    real_data = parse_input(parsing_config, data=raw_real_data)
    _solve_and_check(solve, "Real", real_data, real_answer, wrong_answers)


def to_tuple(*args):
    return tuple(args)
