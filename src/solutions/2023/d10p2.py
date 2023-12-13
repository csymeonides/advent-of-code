from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, Tuple, Set

from utils import run, Example, ParsingConfig


examples = [
    Example(
        answer=4,
        data="""
...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""
    ),
    Example(
        answer=4,
        data="""
..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""
    ),
    Example(
        answer=8,
        data="""
.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""
    ),
    Example(
        answer=10,
        data="""
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""
    )
]


Point = Tuple[float, float]


@dataclass
class Node:
    symbol: str
    neighbours: Set[Point]
    in_loop: bool = False
    can_exit: bool = False
    is_real: bool = True


class Parser:
    def __init__(self):
        self.start: Optional[Point] = None
        self.nodes: Dict[Point, Node] = {}
        self.max_x = 0
        self.max_y = 0

    def parse(self, *line):
        y = self.max_y
        for real_x, char in enumerate(line):
            x = real_x * 2

            if char == "S":
                self.start = (x, y)
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y+1), (x+1, y)}, in_loop=True)
                self.nodes[(x, y+1)] = Node(symbol="|", neighbours={(x, y)}, is_real=False)
                self.nodes[(x+1, y)] = Node(symbol="-", neighbours={(x, y)}, is_real=False)
            elif char == "|":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y+1), (x, y-1)})
                self.nodes[(x, y+1)] = Node(symbol="|", neighbours={(x, y), (x, y+2)}, is_real=False)
                self.nodes[(x+1, y)] = Node(symbol=".", neighbours=set(), is_real=False)
            elif char == "-":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x+1, y), (x-1, y)})
                self.nodes[(x+1, y)] = Node(symbol="-", neighbours={(x, y), (x+2, y)}, is_real=False)
                self.nodes[(x, y+1)] = Node(symbol=".", neighbours=set(), is_real=False)
            elif char == "7":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y+1), (x-1, y)})
                self.nodes[(x, y+1)] = Node(symbol="|", neighbours={(x, y), (x, y+2)}, is_real=False)
                self.nodes[(x+1, y)] = Node(symbol=".", neighbours=set(), is_real=False)
            elif char == "F":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y+1), (x+1, y)})
                self.nodes[(x, y+1)] = Node(symbol="|", neighbours={(x, y), (x, y+2)}, is_real=False)
                self.nodes[(x+1, y)] = Node(symbol="-", neighbours={(x, y), (x+2, y)}, is_real=False)
            elif char == "L":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y-1), (x+1, y)})
                self.nodes[(x, y+1)] = Node(symbol=".", neighbours=set(), is_real=False)
                self.nodes[(x+1, y)] = Node(symbol="-", neighbours={(x, y), (x+2, y)}, is_real=False)
            elif char == "J":
                self.nodes[(x, y)] = Node(symbol=char, neighbours={(x, y-1), (x-1, y)})
                self.nodes[(x, y+1)] = Node(symbol=".", neighbours=set(), is_real=False)
                self.nodes[(x+1, y)] = Node(symbol=".", neighbours=set(), is_real=False)
            elif char == ".":
                self.nodes[(x, y)] = Node(symbol=char, neighbours=set())
                self.nodes[(x, y+1)] = Node(symbol=".", neighbours=set(), is_real=False)
                self.nodes[(x+1, y)] = Node(symbol=".", neighbours=set(), is_real=False)
            self.nodes[(x+1, y+1)] = Node(symbol=".", neighbours=set(), is_real=False)

        self.max_y += 2
        self.max_x = x + 2

    def __str__(self) -> str:
        result = ""
        for yy in range(self.max_y):
            for xx in range(self.max_x):
                node = self.nodes.get((xx, yy))
                if node and node.in_loop:
                    result += f"\033[92m{node.symbol}\033[0m"
                elif node and node.can_exit:
                    result += f"\033[93mO\033[0m"
                elif node and node.is_real:
                    result += "I"
                elif node:
                    result += node.symbol
                else:
                    result += " "
            result += "\n"
        return result


parsing_config = ParsingConfig(
    field_separator="",
    parser_class=Parser,
)


def solve(parser: Parser) -> int:
    queue = [loc for loc, node in parser.nodes.items() if parser.start in node.neighbours]
    queue = [loc for loc, node in parser.nodes.items() if any(q in node.neighbours for q in queue)]
    while queue:
        node = parser.nodes[queue.pop()]
        node.in_loop = True
        for neighbour_loc in node.neighbours:
            neighbour = parser.nodes.get(neighbour_loc)
            if neighbour and not neighbour.in_loop:
                queue.append(neighbour_loc)

    queue = [(x, y) for (x, y), node in parser.nodes.items() if not node.in_loop and (x==0 or y==0 or x==parser.max_x-1 or y==parser.max_y-1)]
    while queue:
        (x, y) = queue.pop()
        node = parser.nodes[(x, y)]
        node.can_exit = True
        for neighbour_loc in [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]:
            if neighbour_loc in parser.nodes:
                neighbour = parser.nodes.get(neighbour_loc)
                if neighbour and not neighbour.in_loop and not neighbour.can_exit:
                    queue.append(neighbour_loc)

    print(parser)

    return len([node for node in parser.nodes.values() if node.is_real and not node.can_exit and not node.in_loop])


if __name__ == "__main__":
    run(
        examples=examples,
        parsing_config=parsing_config,
        solve=solve,
        real_answer=471,
    )
