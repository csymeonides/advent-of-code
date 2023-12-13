from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Dict, Tuple, Set

from utils import run, ParsingConfig, Example

example_answer = 8

example_data = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""


Point = Tuple[int, int]


@dataclass
class Node:
    neighbours: Set[Point]
    dist: Optional[int] = None


class Parser:
    def __init__(self):
        self.start: Optional[Point] = None
        self.nodes: Dict[Point, Node] = {}
        self.n_lines = 0

    def parse(self, *line):
        y = self.n_lines
        for x, char in enumerate(line):
            if char == "S":
                self.start = (x, y)
                node = Node(neighbours=set(), dist=0)
            else:
                if char == "|":
                    node = Node(neighbours={(x, y-1), (x, y+1)})
                elif char == "-":
                    node = Node(neighbours={(x-1, y), (x+1, y)})
                elif char == "L":
                    node = Node(neighbours={(x, y-1), (x+1, y)})
                elif char == "J":
                    node = Node(neighbours={(x-1, y), (x, y-1)})
                elif char == "7":
                    node = Node(neighbours={(x-1, y), (x, y+1)})
                elif char == "F":
                    node = Node(neighbours={(x+1, y), (x, y+1)})
                else:
                    continue
            self.nodes[(x, y)] = node
        self.n_lines += 1

    def print_nodes(self):
        max_x = max(x for (x, y) in self.nodes.keys())
        for y in range(self.n_lines):
            for x in range(max_x + 1):
                if (x, y) in self.nodes:
                    dist = self.nodes[(x, y)].dist
                    print("?" if dist is None else dist, end="")
                else:
                    print(".", end="")
            print()
        print()


parsing_config = ParsingConfig(
    field_separator="",
    parser_class=Parser,
)


def solve(parser: Parser) -> int:
    queue = [loc for loc, node in parser.nodes.items() if parser.start in node.neighbours]
    for loc in queue:
        parser.nodes[loc].dist = 1
    while queue:
        node = parser.nodes[queue.pop()]
        next_dist = (node.dist or 1) + 1
        for neighbour_loc in node.neighbours:
            neighbour = parser.nodes[neighbour_loc]
            if neighbour.dist is None or next_dist < neighbour.dist:
                neighbour.dist = next_dist
                queue.append(neighbour_loc)
    return max(n.dist for n in parser.nodes.values() if n.dist is not None)


if __name__ == "__main__":
    run(
        examples=[Example(answer=example_answer, data=example_data)],
        parsing_config=parsing_config,
        solve=solve,
        real_answer=6875,
    )
