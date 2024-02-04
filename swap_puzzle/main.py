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


# Obtenez le chemin le plus court entre la grille initiale et la grille cible
shortest_path = neighbor_graph.bfs(exemple.transform(), target_grid.transform())

# Affichez le chemin le plus court
print("Shortest Path:", shortest_path)
