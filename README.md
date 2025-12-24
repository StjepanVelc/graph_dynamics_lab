# Graph Dynamics Lab

**Graph Dynamics Lab** is a research-oriented simulation framework for exploring  
**information propagation, correlation, and entanglement-like dynamics on graphs**.

The project is **quantum-inspired**, but deliberately avoids full quantum formalisms  
(Qiskit, density matrices, etc.) in favor of **transparent, interpretable models**  
built from first principles.

---

## Motivation

Graphs are a universal abstraction:
- physical systems
- data networks
- information flow
- interaction structures

This project treats a graph not as static topology, but as a **dynamical system**  
where:
- nodes carry state amplitudes
- edges define interaction rules
- global behavior emerges from local rules

The goal is **understanding dynamics**, not maximizing performance.

---

## Core Concepts

### 1. Graph as Structure
- adjacency matrix with real or complex weights
- directed or undirected edges
- no external graph libraries (custom implementation)

### 2. State as Physics
- each node holds a value (real or complex)
- full state is a normalized vector  
- normalization enforces physical consistency

### 3. Evolution as Law
- deterministic linear evolution rule
- graph acts as an operator on the state
- no hidden randomness

### 4. Time as Simulation
- discrete time steps
- full state history is preserved
- enables post-analysis (entropy, correlation, entanglement)

---

## Metrics & Analysis

The system is analyzed using **information-theoretic and relational measures**:

### Entropy
- Shannon entropy of node probabilities
- tracks information spreading and l

### Future Work

Possible extensions include:

larger and heterogeneous graphs

directed phase-asymmetric dynamics

persistent state logging (CSV / JSON)

C# front-end integration

comparative studies of graph topologies