# simulation/engine.py

from core.state import State
from core.evolution import EvolutionRule


class SimulationEngine:
    def __init__(self, evolution: EvolutionRule, initial_state: State):
        self.evolution = evolution
        self.current_state = initial_state
        self.history = [initial_state]

    def step(self):
        self.current_state = self.evolution.step(self.current_state)
        self.history.append(self.current_state)

    def run(self, steps: int):
        for _ in range(steps):
            self.step()

    def get_state_history(self):
        return self.history
