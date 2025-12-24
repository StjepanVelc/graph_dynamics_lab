import matplotlib.pyplot as plt
from core.metrics import entanglement_over_time


def plot_entanglement_over_time(state_history):
    scores = entanglement_over_time(state_history)

    plt.figure()
    for (i, j), values in scores.items():
        plt.plot(range(len(values)), values, label=f"({i},{j})")

    plt.xlabel("Time step")
    plt.ylabel("Entanglement score")
    plt.title("Entanglement-like correlation over time")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
