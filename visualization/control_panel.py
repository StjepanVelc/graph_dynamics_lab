import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from core.state import State
from core.evolution import EvolutionRule
from simulation.engine import SimulationEngine
from simulation.scenarios import phased_chain_graph
from core.metrics import entropy_over_time


def launch_control_panel():
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    initial = State([1, 0, 0])
    time_steps = 30

    phi_ax = plt.axes([0.2, 0.1, 0.6, 0.03])
    phi_slider = Slider(phi_ax, "Phase φ", 0.0, 1.5, valinit=0.4)

    (line,) = ax.plot([], [])
    ax.set_ylim(0, 2)
    ax.set_xlabel("Time step")
    ax.set_ylabel("Entropy S")

    def update(val):
        phi = phi_slider.val
        g = phased_chain_graph(3, phi)
        engine = SimulationEngine(EvolutionRule(g), initial)
        engine.run(time_steps)

        entropies = entropy_over_time(engine.get_state_history())
        line.set_data(range(len(entropies)), entropies)

        ax.set_xlim(0, len(entropies))
        ax.set_title(f"Entropy over time (φ = {phi:.2f})")
        fig.canvas.draw_idle()

    update(None)
    phi_slider.on_changed(update)
    plt.show()
