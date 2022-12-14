from utils import run, ParsingConfig

example_answer = [19, 23, 23, 29, 26]

example_data = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""


def find_marker(s: str):
    for i in range(14, len(s)):
        if not any(s[j] in s[j+1:i] for j in range(i-14, i-1)):
            return i


parsing_config = ParsingConfig(
    parser_func=find_marker,
    single_field=True,
)


def solve(data):
    return data


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve)
