from utils import run, ParsingConfig, Example

example_answer = 2713310158
n_rounds = 10000

example_data = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""


def _make_operand(val):
    try:
        operand = int(val)
        return lambda x: operand
    except:
        return lambda x: x


def _make_operation(data):
    left = _make_operand(data[0])
    right = _make_operand(data[2])
    operator = data[1]
    if operator == "+":
        return lambda x: left(x) + right(x)
    elif operator == "-":
        return lambda x: left(x) - right(x)
    elif operator == "*":
        return lambda x: left(x) * right(x)
    else:
        return lambda x: left(x) // right(x)


class Monkey:
    def __init__(self, data):
        self.initial_items = [int(d.replace(",", "")) for d in data[1][2:]]
        self.operation = _make_operation(data[2][3:])
        self.divisor = int(data[3][-1])
        self.dest_true = int(data[4][-1])
        self.dest_false = int(data[5][-1])
        self.total_inspected = 0
        self.items = []

    def pass_items(self):
        self.total_inspected += len(self.items)
        for item in self.items:
            item.update(self.operation)
        destinations = [(item, self.dest_true if item.is_divisible_by(self.divisor) else self.dest_false) for item in self.items]
        self.items = []
        return destinations


parsing_config = ParsingConfig(
    parser_func=Monkey,
    multi_line=True,
)


class Item:
    def __init__(self, value, divisors):
        self.value = {divisor: value % divisor for divisor in divisors}

    def update(self, operation):
        for divisor in self.value.keys():
            self.value[divisor] = operation(self.value[divisor]) % divisor

    def is_divisible_by(self, divisor):
        return self.value[divisor] == 0


def solve(data):
    divisors = [m.divisor for m in data]
    for monkey in data:
        monkey.items = [Item(val, divisors) for val in monkey.initial_items]

    for i in range(n_rounds):
        for monkey in data:
            for (item, destination) in monkey.pass_items():
                data[destination].items.append(item)

    top2 = sorted([m.total_inspected for m in data])[-2:]
    return top2[0] * top2[1]


real_answer = 20151213744


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
