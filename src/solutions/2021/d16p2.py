from enum import Enum
from math import prod
from typing import List

from utils import run, ParsingConfig, Example

example_answer = 1

example_data = """
9C0141080250320F1802104A08
"""


def bin_to_dec(bin_string) -> int:
    return int(bin_string, 2)


def hex_to_bin(hex_char) -> str:
    return f"{int(hex_char, 16):04b}"


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL = 4
    GREATER_THAN = 5
    LESS_THAN = 6
    EQUAL_TO = 7


class Packet:
    def __init__(self, *bin_chars):
        bin_string = "".join(bin_chars)
        self.version = bin_to_dec(bin_string[:3])
        self.packet_type = bin_to_dec(bin_string[3:6])
        self.subpackets = []
        self.version_sum = self.version

        if self.packet_type == PacketType.LITERAL.value:
            i = 6
            value_string = ""
            while bin_string[i] != "0":
                value_string += bin_string[i+1:i+5]
                i += 5
            value_string += bin_string[i+1:i+5]
            self.remainder = bin_string[i+5:]
            self.value = bin_to_dec(value_string)

        else:
            length_type = bin_to_dec(bin_string[6])
            if length_type == 0:
                subpacket_length = bin_to_dec(bin_string[7:22])
                subpacket_string = bin_string[22:22 + subpacket_length]
                self.remainder = bin_string[22 + subpacket_length:]
                while len(subpacket_string) >= 11:
                    subpacket = Packet(subpacket_string)
                    self.subpackets.append(subpacket)
                    self.version_sum += subpacket.version_sum
                    subpacket_string = subpacket.remainder

            else:
                n_subpackets = bin_to_dec(bin_string[7:18])
                self.remainder = bin_string[18:]
                for _ in range(n_subpackets):
                    subpacket = Packet(self.remainder)
                    self.subpackets.append(subpacket)
                    self.version_sum += subpacket.version_sum
                    self.remainder = subpacket.remainder

            if self.packet_type == PacketType.SUM.value:
                self.value = sum(p.value for p in self.subpackets)
            elif self.packet_type == PacketType.PRODUCT.value:
                self.value = prod(p.value for p in self.subpackets)
            elif self.packet_type == PacketType.MIN.value:
                self.value = min(p.value for p in self.subpackets)
            elif self.packet_type == PacketType.MAX.value:
                self.value = max(p.value for p in self.subpackets)
            elif self.packet_type == PacketType.GREATER_THAN.value:
                self.value = 1 if self.subpackets[0].value > self.subpackets[1].value else 0
            elif self.packet_type == PacketType.LESS_THAN.value:
                self.value = 1 if self.subpackets[0].value < self.subpackets[1].value else 0
            elif self.packet_type == PacketType.EQUAL_TO.value:
                self.value = 1 if self.subpackets[0].value == self.subpackets[1].value else 0


parsing_config = ParsingConfig(
    parser_func=Packet,
    field_separator="",
    value_converter=hex_to_bin,
)


def solve(data: List[Packet]):
    return data[0].value


real_answer = 12883091136209


if __name__ == "__main__":
    run([Example(answer=example_answer, data=example_data)], parsing_config, solve, real_answer)
