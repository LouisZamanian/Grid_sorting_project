from grid import Grid

#g = Grid(2, 3)
#print(g)

data_path = "../input/"
file_name = data_path + "grid0.in"

#print(file_name)
#print("bonjour")
#g = Grid.grid_from_file(file_name)
#print(g)

exemple = Grid(2, 2, [[4, 3], [1, 2]])

# Obtenez le graphe des voisins
neighbor_graph = exemple.next_neighbors()

# Grille cible
target_grid = Grid(2, 2, [[1, 2], [3, 4]])

# Create the neighbor graph
neighbor_graph, arretes, noeuds = exemple.next_neighbors()

# Obtain the shortest path between the initial and target grids
shortest_path = neighbor_graph.bfs(exemple.transform(), target_grid.transform())

# Display the shortest path
print("Shortest Path:", shortest_path)
print("arretes",arretes)
print("noeuds",noeuds)
