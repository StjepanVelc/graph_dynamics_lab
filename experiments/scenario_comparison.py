from core.state import State
from core.evolution import EvolutionRule
from simulation.engine import SimulationEngine
from core.metrics import entropy_over_time
from simulation.scenarios import chain_graph, phased_chain_graph
import matplotlib.pyplot as plt


def compare_scenarios():
    scenarios = {
        "Chain (no phase)": chain_graph(3),
        "Chain (phase φ=0.4)": phased_chain_graph(3, phi=0.4),
    }

    initial = State([1, 0, 0])

    plt.figure()

    for name, graph in scenarios.items():
        engine = SimulationEngine(EvolutionRule(graph), initial)
        engine.run(25)

        entropies = entropy_over_time(engine.get_state_history())
        plt.plot(entropies, label=name)

    plt.xlabel("Time step")
    plt.ylabel("Entropy S")
    plt.title("Scenario comparison — entropy over time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
