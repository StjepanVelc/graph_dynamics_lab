from core.graph import Graph
import cmath


def chain_graph(n: int):
    g = Graph(n)
    for i in range(n - 1):
        g.add_undirected_edge(i, i + 1)
    return g


def phased_chain_graph(n: int, phi: float):
    g = Graph(n)
    for i in range(n - 1):
        g.add_edge(i, i + 1, cmath.exp(1j * phi))
        g.add_edge(i + 1, i, cmath.exp(-1j * phi))
    return g
