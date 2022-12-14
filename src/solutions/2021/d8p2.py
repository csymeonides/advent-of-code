from utils import run, ParsingConfig

example_answer = 61229

example_data = """
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


def parse(first, second):
    return first.split(), second.split()


parsing_config = ParsingConfig(
    parser_func=parse,
    field_separator=" | ",
)


def _decode(first, second):
    digisets = [set(d for d in digit) for digit in first]

    one_cf = next(d for d in digisets if len(d) == 2)
    four_bdcf = next(d for d in digisets if len(d) == 4)
    seven_acf = next(d for d in digisets if len(d) == 3)

    only_256 = [d for d in digisets if not one_cf.issubset(d)]
    six = next(d for d in only_256 if len(d) == 6)

    eight = set(d for d in "abcdefg")
    c = eight - six
    a = seven_acf - one_cf
    f = seven_acf - a - c

    five = next(d for d in only_256 if d != six and f.issubset(d))
    two = next(d for d in only_256 if d not in [five, six])
    nine = five.union(c)

    only_03 = [d for d in digisets if d not in [one_cf, two, four_bdcf, five, six, seven_acf, eight, nine]]
    zero = next(d for d in only_03 if len(d) == 6)
    three = next(d for d in only_03 if len(d) == 5)

    digits = [
        zero,
        one_cf,
        two,
        three,
        four_bdcf,
        five,
        six,
        seven_acf,
        eight,
        nine,
    ]

    decoded = [digits.index(set(d for d in digit)) for digit in second]
    return sum(d * 10**i for i, d in enumerate(reversed(decoded)))


def solve(data):
    return sum([_decode(first, second) for first, second in data])


real_answer = 908067


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
