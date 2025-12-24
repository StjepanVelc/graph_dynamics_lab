class Graph:
    def __init__(self, num_nodes: int):
        self.num_nodes = num_nodes

        # adjacency matrix (weight-based)
        self.adjacency = [[0.0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, i: int, j: int, weight: float = 1.0):
        """Add a directed edge i -> j."""
        self._validate_node(i)
        self._validate_node(j)
        self.adjacency[i][j] = weight

    def add_undirected_edge(self, i: int, j: int, weight: float = 1.0):
        """Add an undirected edge between i and j."""
        self.add_edge(i, j, weight)
        self.add_edge(j, i, weight)

    def neighbors(self, i: int):
        """Return indices of neighboring nodes."""
        self._validate_node(i)
        return [j for j, weight in enumerate(self.adjacency[i]) if weight != 0]

    def get_weight(self, i: int, j: int):
        self._validate_node(i)
        self._validate_node(j)
        return self.adjacency[i][j]

    def _validate_node(self, i: int):
        if not 0 <= i < self.num_nodes:
            raise IndexError(f"Node {i} is out of bounds.")

    def __repr__(self):
        return f"Graph(num_nodes={self.num_nodes})"
