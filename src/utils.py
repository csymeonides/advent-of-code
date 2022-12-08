import os
import sys
import time
from dataclasses import dataclass

import requests

from contextlib import contextmanager
from typing import List, Union, Optional, Type, Callable


def check(answer_function, input, expected):
    result = answer_function(input)
    assert result == expected, f"Expected {expected} but was {result}"


def _pass_through(single_field: bool):
    if single_field:
        return lambda arg: arg
    else:
        return lambda *args: list(args)


def get_input_data() -> List[str]:
    calling_script = sys.argv[0]
    script_dir = os.path.dirname(calling_script)
    year = os.path.basename(script_dir)
    day = os.path.basename(calling_script).split("p")[0][1:]

    data_file = f"{script_dir}/d{day}.data"
    if not os.path.exists(data_file):
        data_url = f"https://adventofcode.com/{year}/day/{day}/input"
        token = open(f"{os.path.dirname(os.path.abspath(__file__))}/.token").readline().strip()
        response = requests.get(data_url, cookies={"session": token}, timeout=5)
        with open(data_file, "w") as file:
            file.write(response.text)

    return open(data_file).read().splitlines()


@dataclass
class ParsingConfig:
    strip: bool = True  # whether to trim whitespace from each line of the input
    field_separator: Optional[str] = None  # how to divide each line into fields (default: any whitespace)
    single_field: bool = False  # whether each line contains only 1 field
    value_converter: Optional[Callable] = None  # called for each field, e.g. to convert strings to ints
    multi_line: Union[bool, int] = False  # True=each record consists of multiple lines, separated by an empty line. int=each record consists of N lines, no empty line between them
    parser_func: Optional[Callable] = None  # called for each record, with an arg for each field
    parser_class: Optional[Type] = None  # for stateful parsing, must implement a parse() method to be called per record (same as parser_func)


def parse_input(config: ParsingConfig, example_data: str = None):
    if config.parser_class is not None and config.parser_func is not None:
        raise ValueError("You cannot specify both parser_func and parser_class")

    if config.parser_class is not None:
        parser_func = config.parser_class().parse
    elif config.parser_func is not None:
        parser_func = config.parser_func
    else:
        parser_func = _pass_through(config.single_field)

    if example_data:
        data = example_data.split("\n")
        if data[0] == "":
            data = data[1:]
        if data[-1] == "":
            data = data[:-1]
    else:
        data = get_input_data()

    records = []
    multi_line_vals = []
    for line in data:
        if config.strip:
            line = line.strip()

        if not line:
            vals = []
        elif config.single_field:
            vals = [line]
        elif config.field_separator is None:
            vals = line.split()
        elif config.field_separator == "":
            vals = list(line)  # splits a string into a list of chars
        else:
            vals = line.split(config.field_separator)

        if config.value_converter is not None:
            vals = [config.value_converter(val) for val in vals]

        if config.multi_line:
            if line == "":
                if multi_line_vals:
                    record = parser_func(multi_line_vals)
                    records.append(record)
                    multi_line_vals = []
            else:
                multi_line_vals.append(vals[0] if config.single_field else vals)
                if not isinstance(config.multi_line, bool) and len(multi_line_vals) == config.multi_line:
                    record = parser_func(multi_line_vals)
                    records.append(record)
                    multi_line_vals = []
        elif vals:
            record = parser_func(*vals)
            records.append(record)

    if config.multi_line and multi_line_vals:
        # Final record
        record = parser_func(multi_line_vals)
        records.append(record)

    return records


@contextmanager
def timer(label):
    start_time = time.time()
    try:
        yield
    finally:
        elapsed = (time.time() - start_time)
        print(f"{label} took {elapsed:.1}s to solve")


def check_example_and_get_actual_answer(example_data, example_answer, parsing_config, solve):
    example_data = parse_input(parsing_config, example_data=example_data)
    with timer("Example"):
        actual = solve(example_data)
        assert example_answer == actual, f"Expected {example_answer} but got {actual}"

    real_data = parse_input(parsing_config)
    with timer("Real"):
        answer = solve(real_data)
    print(f"Answer: {answer}")
