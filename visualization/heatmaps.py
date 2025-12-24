import matplotlib.pyplot as plt
import numpy as np
from core.state import State
from matplotlib.animation import FuncAnimation

def correlation_matrix(state: State):
    n = len(state)
    C = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            C[i, j] = abs(state.values[i] * state.values[j].conjugate())

    return C


def plot_correlation_heatmap(state: State, title: str = ""):
    C = correlation_matrix(state)

    plt.figure()
    plt.imshow(C, cmap="inferno")
    plt.colorbar(label="Correlation")
    plt.title(title)
    plt.xlabel("Node j")
    plt.ylabel("Node i")
    plt.tight_layout()
    plt.show()


def animate_correlation_history(state_history):
    fig, ax = plt.subplots()
    C0 = correlation_matrix(state_history[0])

    img = ax.imshow(C0, cmap="inferno", vmin=0, vmax=1)
    plt.colorbar(img, ax=ax, label="Correlation")

    ax.set_xlabel("Node j")
    ax.set_ylabel("Node i")

    def update(frame):
        C = correlation_matrix(state_history[frame])
        img.set_data(C)
        ax.set_title(f"Correlation heatmap — t = {frame}")
        return [img]

    ani = FuncAnimation(
        fig, update, frames=len(state_history), interval=800, repeat=True
    )

    plt.tight_layout()
    plt.show()
