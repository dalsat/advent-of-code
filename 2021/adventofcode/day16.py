from __future__ import annotations
from abc import abstractclassmethod
from dataclasses import dataclass
from functools import reduce

from common import day, Dataset, Solution
from common.typing import Char


class PacketParser:

    @classmethod
    def hex_to_bin(cls, hex_char: Char):
        return bin(int(hex_char, 16))[2:].zfill(4)

    def __init__(self, packet: str):
        self.packet = packet
        self.packet_iter = iter(self.packet)
        self.read_counter = 0

    @classmethod
    def parse_hex(cls, hex_packet: str):
        bin_packet = ''.join(map(cls.hex_to_bin, hex_packet))
        return PacketParser(bin_packet).parse()

    def read(self, bits: int=1):
        self.read_counter += bits
        return ''.join(next(self.packet_iter) for _ in range(bits))
    
    def read_int(self, bits: int=1):
        return int(self.read(bits), 2)
        
    def parse(self) -> Packet:
        version = self.read_int(3)
        type_id = self.read_int(3)

        if type_id == 4:
            return self.parse_literal_packet(version, type_id)
        else:
            return self.parse_operator_packet(version, type_id)


    def parse_literal_packet(self, version: int, type_id: int):
        at_end = False
        bits = []

        while not at_end:
            at_end = not bool(self.read_int())
            bits.append(str(self.read(4)))

        return LiteralPacket(
            version,
            type_id,
            int(''.join(bits), 2)
        )


    def parse_operator_packet(self, version: int, type_id: int) -> OperatorPacket:
        length_type_id = self.read_int()
        if length_type_id == 0:  # length_type_id
            bits_length = self.read_int(15)
            bits_to_read = self.read_counter + bits_length
            subpackets = []
            while self.read_counter < bits_to_read:
                subpackets.append(self.parse())
        else:
            subpackets = [self.parse() for _ in range(self.read_int(11))]

        return OperatorPacket(
            version,
            type_id,
            length_type_id,
            subpackets
        )


@dataclass
class Packet:
    version: int
    type_id: int

    def version_sum(self):
        return self.version
    
    @abstractclassmethod
    def eval(self):
        pass

    
@dataclass
class LiteralPacket(Packet):
    literal: int

    def eval(self):
        return self.literal

    def print(self):
        return self.literal


@dataclass
class OperatorPacket(Packet):
    length_type_id: int
    packets: Packet

    def version_sum(self):
        return self.version + sum(sub.version_sum() for sub in self.packets)

    def eval(self):
        sub_eval = tuple(sub.eval() for sub in self.packets)
        if self.type_id == 0:
            return sum(sub_eval)
        elif self.type_id == 1:
            return reduce(lambda a, b: a * b, sub_eval, 1)
        elif self.type_id == 2:
            return min(sub_eval)
        elif self.type_id == 3:
            return max(sub_eval)
        elif self.type_id == 5:
            assert len(sub_eval) == 2
            return int(sub_eval[0] > sub_eval[1])
        elif self.type_id == 6:
            assert len(sub_eval) == 2
            return int(sub_eval[0] < sub_eval[1])
        elif self.type_id == 7:
            assert len(sub_eval) == 2
            return int(sub_eval[0] == sub_eval[1])

    def print(self):
        sub_eval = ', '.join(str(sub.print()) for sub in self.packets)
        if self.type_id == 0:
            return f'sum({sub_eval})'
        elif self.type_id == 1:
            return f'prod({sub_eval})'
        elif self.type_id == 2:
            return f'min({sub_eval})'
        elif self.type_id == 3:
            return f'max({sub_eval})'
        elif self.type_id == 5:
            return f'gt({sub_eval})'
        elif self.type_id == 6:
            return f'lt({sub_eval})'
        elif self.type_id == 7:
            return f'eq({sub_eval})'


def run() -> tuple(Solution, Solution):
    data: Dataset = day(16)
    packet = PacketParser.parse_hex(data)
    return (
        packet.version_sum(),
        packet.eval()
    )

if __name__ == '__main__':
    print(run())
