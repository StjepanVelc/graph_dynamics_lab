import matplotlib.pyplot as plt
from core.state import State
from matplotlib.animation import FuncAnimation


def plot_state(state: State, title: str = ""):
    magnitudes = [abs(v) for v in state.values]
    nodes = list(range(len(magnitudes)))

    plt.figure()
    plt.bar(nodes, magnitudes)
    plt.ylim(0, 1)
    plt.xlabel("Node")
    plt.ylabel("|ψ|")
    plt.title(title)
    plt.show()


def animate_state_history(state_history):
    fig, ax = plt.subplots()
    nodes = list(range(len(state_history[0].values)))
    bars = ax.bar(nodes, [0] * len(nodes))

    ax.set_ylim(0, 1)
    ax.set_xlabel("Node")
    ax.set_ylabel("|ψ|")

    def update(frame):
        state = state_history[frame]
        magnitudes = [abs(v) for v in state.values]
        for bar, mag in zip(bars, magnitudes):
            bar.set_height(mag)
        ax.set_title(f"t = {frame}")
        return bars

    ani = FuncAnimation(
        fig, update, frames=len(state_history), interval=800, repeat=True
    )

    plt.show()
