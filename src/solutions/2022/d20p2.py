from typing import List

from utils import run, ParsingConfig

example_answer = 1623178306

example_data = """
1
2
-3
3
-2
0
4
"""


parsing_config = ParsingConfig(
    single_field=True,
    value_converter=int,
)


def solve(data: List[int]) -> int:
    data = [v * 811589153 for v in data]
    n = len(data)
    llist = list(range(n))
    expected_vals = [
        [2, 1, -3, 3, -2, 0, 4],
        [1, -3, 2, 3, -2, 0, 4],
        [1, 2, 3, -2, -3, 0, 4],
        [1, 2, -2, -3, 0, 3, 4],
        [1, 2, -3, 0, 3, 4, -2],
        [1, 2, -3, 0, 3, 4, -2],
        [1, 2, -3, 4, 0, 3, -2],
    ]
    for _ in range(10):
        for i, val in enumerate(data):
            val_index = llist.index(i)
            llist.pop(val_index)
            new_index = (val_index + val) % (n - 1)
            if new_index == 0:
                llist.append(i)
            else:
                llist.insert(new_index, i)
            # assert [data[j] for j in llist] == expected_vals[i], f"Expected {expected_vals[i]} but was {[data[j] for j in llist]}"
    zero_index = llist.index(data.index(0))
    return data[llist[(1000 + zero_index) % n]] + data[llist[(2000 + zero_index) % n]] + data[llist[(3000 + zero_index) % n]]


if __name__ == "__main__":
    run(
        example_data, example_answer, parsing_config, solve,
        wrong_answers=[-4258, -1624],
        real_answer=2897373276210,
    )
