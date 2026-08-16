import operator

import numpy as np
import numpy.typing as npt
from common import day


def power_consumption(data: list[str]) -> int:
    matrix = np.asmatrix([np.fromiter(each, dtype=int) for each in data])
    threshold = len(matrix) // 2
    counts = sum(matrix)

    def filter(x):
        return x > threshold

    filter_vec = np.vectorize(filter)

    most_common_bits = np.squeeze(np.asarray(filter_vec(counts)))

    gamma = bin_to_number(most_common_bits.astype(int))
    epsilon = bin_to_number(np.logical_not(most_common_bits).astype(int))
    return gamma * epsilon


def bin_to_number(bin_array: npt.NDArray) -> int:
    return int("".join(bin_array.astype(str)), base=2)


class LifeSupportRating:
    def __init__(self, data: list[str]) -> None:
        self.bits = np.asarray([np.fromiter(each, dtype=int) for each in data])
        self.bits_size = len(data[0])

    @classmethod
    def filter_most_common_bit(cls, bits, index, filter_criteria):
        most_common_bit = int(filter_criteria(sum(bits[:, index]), len(bits) / 2))
        return bits[bits[:, index] == most_common_bit]

    def compute_value(self, filter_criteria) -> int:
        bits = self.bits
        for i in range(self.bits_size):
            bits = self.filter_most_common_bit(bits, i, filter_criteria)
            if len(bits) == 1:
                return bin_to_number(bits[0])
        raise ValueError("value not found")

    @property
    def oxygen_generator_rating(self) -> int:
        return self.compute_value(operator.ge)

    @property
    def co2_scrubber_rating(self) -> int:
        return self.compute_value(operator.lt)

    @property
    def value(self) -> int:
        return self.oxygen_generator_rating * self.co2_scrubber_rating


def run() -> tuple[int, int]:
    data = day(3)
    return (power_consumption(data), LifeSupportRating(data).value)


print(run())
