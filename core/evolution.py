from core.graph import Graph
from core.state import State


class EvolutionRule:
    def __init__(self, graph: Graph):
        self.graph = graph

    def step(self, state: State) -> State:
        """Compute next state from current state."""
        if len(state) != self.graph.num_nodes:
            raise ValueError("State size does not match graph.")

        new_values = [0 for _ in range(self.graph.num_nodes)]

        for i in range(self.graph.num_nodes):
            total = 0
            for j in self.graph.neighbors(i):
                weight = self.graph.get_weight(j, i)
                total += weight * state.values[j]
            new_values[i] = total

        return State(new_values)
