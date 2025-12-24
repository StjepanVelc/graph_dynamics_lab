# core/metrics.py

import math
from core.state import State


def entropy(state: State) -> float:
    """Shannon entropy of state probabilities."""
    probs = [abs(v) ** 2 for v in state.values]
    s = 0.0
    for p in probs:
        if p > 0:
            s -= p * math.log2(p)
    return s


def magnitudes(state: State):
    """Return magnitudes of all nodes."""
    return [abs(v) for v in state.values]


def entropy_over_time(state_history):
    return [entropy(state) for state in state_history]


def entanglement_score(state, i, j):
    """Entanglement-like score between node i and j."""
    return abs(state.values[i] * state.values[j].conjugate())


def entanglement_over_time(state_history):
    """Compute entanglement scores for all node pairs over time."""
    n = len(state_history[0])
    scores = {(i, j): [] for i in range(n) for j in range(i + 1, n)}

    for state in state_history:
        for i, j in scores:
            scores[(i, j)].append(entanglement_score(state, i, j))

    return scores
