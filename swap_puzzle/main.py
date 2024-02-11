from grid import Grid
from solver import Solver

#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

#print(file_name)
#print("bonjour")
#g = Grid.grid_from_file(file_name)
#print(g)

exemple = Grid(2, 2, [[1,6], [3,5]])

exp=Grid(2,2,[[1,2],[3,4]])
exp.generate_all_grid_states()
print(exp.generate_all_grid_states())


# Obtenez le graphe des voisins
#neighbor_graph = exemple.next_neighbors()

# Grille cible
#target_grid = Grid(2,2, [[1,3],[5,6]])

# Create the neighbor graph
#neighbor_graph, arretes, noeuds = exemple.next_neighbors_new()

# Obtain the shortest path between the initial and target grids
#shortest_path = neighbor_graph.bfs(exemple.transform(), target_grid.transform())


# Display the shortest path
#print("Shortest Path:", shortest_path)
#print("arretes",arretes)
#print("noeuds",noeuds)

# Créez une instance de la classe Solver avec les dimensions de la grille et l'état initial
exemple_solver = Solver(2, 2, initial_state=[[1, 3], [4, 2]])

# Appelez la méthode get_solution pour obtenir la solution du puzzle
#nombre_swaps, sequence_swaps = exemple_solver.get_solution()

# Affichez les résultats
#print("Nombre de swaps nécessaires :", nombre_swaps)
#print("Sequence de swaps :", sequence_swaps)
#print(len(shortest_path))
