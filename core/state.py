import math
from typing import List, Union


Number = Union[float, complex]


class State:
    def __init__(self, values: List[Number]):
        self.values = values
        self.normalize()

    def normalize(self):
        """Normalize the state vector."""
        norm = math.sqrt(sum(abs(v) ** 2 for v in self.values))
        if norm == 0:
            raise ValueError("Cannot normalize zero state.")
        self.values = [v / norm for v in self.values]

    def magnitude(self, i: int) -> float:
        return abs(self.values[i])

    def phase(self, i: int) -> float:
        v = self.values[i]
        if isinstance(v, complex):
            return math.atan2(v.imag, v.real)
        return 0.0

    def copy(self):
        return State(self.values.copy())

    def __len__(self):
        return len(self.values)

    def __repr__(self):
        return f"State(values={self.values})"
