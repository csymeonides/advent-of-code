from utils import run, ParsingConfig, Example

example_answer = [7, 5, 6, 10, 11]

example_data = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
bvwbjplbgvbhsrlpgdmjqwftvncz
nppdvjthqldpwncqszvftbrmjlhg
nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg
zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
"""


def find_marker(s: str):
    for i in range(4, len(s)):
        if s[i-4] not in s[i-3:i] and s[i-3] not in s[i-2:i] and s[i-2] != s[i-1]:
            return i


parsing_config = ParsingConfig(
    parser_func=find_marker,
    single_field=True,
)


def solve(data):
    return data


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve)
