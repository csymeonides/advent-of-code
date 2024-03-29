import time
from contextlib import contextmanager
from dataclasses import dataclass
from typing import List

from utils.fetcher import get_input_data, check_real_answer
from utils.parser import parse_input


@dataclass
class Example:
    answer: int
    data: str


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


def _solve_and_check(solve, label, data, expected, too_high=None, too_low=None):
    with timer(label):
        answer = solve(data)
    if expected is None:
        print(f"Answer: {answer}")
        if label == "Real":
            if too_high is not None and answer >= too_high:
                print("Too high!")
            elif too_low is not None and answer <= too_low:
                print("Too low!")
            else:
                check_real_answer(answer)
    else:
        assert expected == answer, f"Expected {expected} but got {answer}"
        print(f"CORRECT! Answer: {answer}")


def run(examples: List[Example], parsing_config, solve, real_answer=None, too_high=None, too_low=None):
    raw_real_data = get_input_data()

    for i, example in enumerate(examples):
        example_data = parse_input(parsing_config, data=prepare_example_data(example.data))
        _solve_and_check(solve, f"Example {i}", example_data, example.answer)
        print()

    real_data = parse_input(parsing_config, data=raw_real_data)
    _solve_and_check(solve, "Real", real_data, real_answer, too_high, too_low)


def to_tuple(*args):
    return tuple(args)
