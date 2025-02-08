# Grid Sorting Project

## Description
This project, developed as part of the [ENSAE 1A 2023-2024] program, explores algorithms and approaches to solve a grid sorting puzzle (**swap puzzle**). The project is based on a modular Python implementation and covers aspects ranging from problem modeling to optimized solutions.

---

## Technical Features
- **Grid Generation**:
  - Creation of random \( n \times n \) grids with initial values.
  - Visualization of the initial grid states.
  
- **Solving Algorithms**:
  - Implementation of various algorithms (DFS, BFS, A*, specific heuristics).
  - Performance comparison of solutions across multiple configurations.
  
- **Graphs and Data Structures**:
  - Use of graphs to model possible movements on the grid.
  - Graph traversal to identify the optimal solution.

---

## Project Structure


```
Grid_sorting_project/ 
├── input/ # Input data (files, configurations) 
├── swap_puzzle/ # Python modules for solving the puzzle 
│ ├── creation_jeu.py # Grid generation 
│ ├── graph.py # Graph management 
│ ├── grid.py # Grid and movement modeling 
│ ├── solver.py # Solving algorithms 
│ ├── main.py # Main entry point 
├── Notebooks/ # Jupyter notebooks for analysis 
├── tests/ # Unit testing scripts 
├── README.md # Project documentation 
└── requirements.txt # List of Python dependencies
```




---

## Implemented Algorithms
### 1. Depth-First Search (DFS)
- Used to exhaustively explore all possible paths.
- Limited by the risk of infinite cycles.

### 2. Breadth-First Search (BFS)
- Allows finding the shortest path in the grid graph.
- Requires more memory than DFS.

### 3. A* with Heuristic
- Combines the path cost and an estimate of the remaining cost.
- Heuristic used: Manhattan distance.

---

## Authors
- **Louis Zamanian**: Lead developer
