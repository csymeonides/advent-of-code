from typing import List

from utils import run, ParsingConfig

example_answer = 31

example_data = """
A0016C880162017C3686B18A3D4780
"""


def bin_to_dec(bin_string) -> int:
    return int(bin_string, 2)


def hex_to_bin(hex_char) -> str:
    return f"{int(hex_char, 16):04b}"


LITERAL = 4


class Packet:
    def __init__(self, *bin_chars):
        bin_string = "".join(bin_chars)
        self.version = bin_to_dec(bin_string[:3])
        self.packet_type = bin_to_dec(bin_string[3:6])
        self.subpackets = []
        self.version_sum = self.version

        if self.packet_type == LITERAL:
            i = 6
            while bin_string[i] != "0":
                i += 5
            self.remainder = bin_string[i+5:]

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


parsing_config = ParsingConfig(
    parser_func=Packet,
    field_separator="",
    value_converter=hex_to_bin,
)


def solve(data: List[Packet]):
    return data[0].version_sum


real_answer = 967


if __name__ == "__main__":
    run(example_data, example_answer, parsing_config, solve, real_answer)
