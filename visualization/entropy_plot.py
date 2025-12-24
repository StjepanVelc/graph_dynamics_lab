import matplotlib.pyplot as plt
from core.metrics import entropy_over_time


def plot_entropy_over_time(state_history):
    entropies = entropy_over_time(state_history)
    time = list(range(len(entropies)))

    plt.figure()
    plt.plot(time, entropies, marker="o")
    plt.xlabel("Time step")
    plt.ylabel("Entropy S")
    plt.title("Entropy over time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
