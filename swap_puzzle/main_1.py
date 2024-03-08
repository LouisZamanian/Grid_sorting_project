from grid import Grid
from solver import Solver
import time
import random
t1=time.time()
#g = Grid(2, 3)
#print(g)
data_path = "../input/"
file_name = data_path + "grid0.in"

#print(file_name)
#print("bonjour")
#g = Grid.grid_from_file(file_name)
#print(g)
exemple=Grid(4,4,[[1,16,14,12],[13,11,10,9],[5,2,8,3],[4,6,7,15]])
exemple=Grid(3,3,[[1,3,4],[2,6,5],[9,8,7]])

def creer_matrice(n, m):
    return [[i + j * m + 1 for i in range(m)] for j in range(n)]

#print(creer_matrice(2,3))
def generate_random_grid(m, n):
    numbers = list(range(1, m * n + 1))
    random.shuffle(numbers)
    return Grid(m,n,[numbers[i:i + n] for i in range(0, len(numbers), n)])

def generate_10_grids(nb, m, n):
    target_grid = Grid(m, n, [[i + j * n + 1 for i in range(n)] for j in range(m)])

    for i in range(nb):
        grid = Grid(m, n, generate_random_grid(m, n))
        neighbor_graph, arretes, noeuds = grid.a_star()
        shortest_path = neighbor_graph.bfs(grid.transform(), target_grid.transform())
        print(grid.state, len(shortest_path))
    return

#print(generate_10_grids(10,3,3))
#exemple=Grid(4,4,generate_random_grid(4,4))
#exemple=Grid(4,4,[[1,4,2,3],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#exemple = Grid(3,3, [[1,5,3],[4,2,6],[9,7,8]])
exemple=generate_random_grid(3,3)
print(exemple)
#exp=Grid(2,2,[[1,2],[3,4]])

#exp.generate_all_grid_states()
#print(exp.generate_all_grid_states())

# Obtenez le graphe des voisins
#neighbor_graph = exemple.a_star()

# Grille cible
#target_grid = Grid(4,4, [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
#target_grid=Grid(4,4,[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
target_grid=Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])


# Create the neighbor graph
neighbor_graph, arretes, noeuds = exemple.a_star_new_new()
#neighbor_graph, arretes, noeuds = exemple.next_neighbors_new()

# Obtain the shortest path between the initial and target grids
shortest_path = neighbor_graph.bfs(exemple.transform(), target_grid.transform())


# Display the shortest path
print("Shortest Path:", shortest_path)
print("arretes",arretes)
print("noeuds",noeuds)
t2=time.time()
print("temps",t2-t1)

# Créez une instance de la classe Solver avec les dimensions de la grille et l'état initial
#exemple_solver = Solver(2, 2, initial_state=[[1, 3], [4, 2]])

# Appelez la méthode get_solution pour obtenir la solution du puzzle
#nombre_swaps, sequence_swaps = exemple_solver.get_solution()

# Affichez les résultats
#print("Nombre de swaps nécessaires :", nombre_swaps)
#print("Sequence de swaps :", sequence_swaps)
#print(len(shortest_path))
