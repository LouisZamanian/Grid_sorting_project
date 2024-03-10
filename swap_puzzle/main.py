from grid import Grid
from solver import Solver
import time
import random
t1=time.time()
#g = Grid(2, 3)
#print(g)
data_path = "../input/"
file_name = data_path + "grid0.in"


#fonctions utiles pour faire les tests
def creer_matrice(m, n):
    return Grid(m, n, [[i + j * n + 1 for i in range(n)] for j in range(m)])

def generate_random_grid(m, n):
    numbers = list(range(1, m * n + 1))
    random.shuffle(numbers)
    return Grid(m,n,[numbers[i:i + n] for i in range(0, len(numbers), n)])

def generate_10_grids(nb, m, n):
    target_grid = Grid(m, n, [[i + j * n + 1 for i in range(n)] for j in range(m)])

    for i in range(nb):
        grid = Grid(m, n, generate_random_grid(m, n))
        neighbor_graph, arretes, noeuds = grid.a_star_final_heapq()
        shortest_path = neighbor_graph.bfs(grid.transform(), target_grid.transform())
        print(grid.state, len(shortest_path))
    return

#Test des programmes avec des grilles aléatoires
#exemple=generate_random_grid(8,8)
exemple=Grid(2,3,[[6,2,3],[4,5,1]])
print(exemple)

# Grille cible
target_grid=creer_matrice(2,3)
print(target_grid)
#target_grid=Grid(3,3,[[1,2,3],[4,5,6],[7,8,9]])

# Question n°3
#Test de la fonction
#grid1= Solver(2, 3, [[6, 2,3], [4, 5,1]])
#grid2=Solver(2,2,[[1,3],[4,2]])
#print(grid1.get_solution())

# Obtenir le graphe des voisins
#questionn°7:
#neighbor_graph, arretes, noeuds=exemple.generate_all_grid_states()

#question n°8:
#neighbor_graph, arretes, noeuds=exemple.next_neighbors_new()

#Séance 3 : Question n°1
neighbor_graph, arretes, noeuds = exemple.a_star_final_heapq()


#On applique ensuite bfs sur le graphe
shortest_path = neighbor_graph.bfs(exemple.transform(), target_grid.transform())

# Affichage des résultats
print("Shortest Path:", shortest_path)
print("Nombre de swaps :",len(shortest_path)-1)
print("arretes",arretes)
print("noeuds",noeuds)
t2=time.time()
print("temps",t2-t1)



# Affichage des résultats
#print("Nombre de swaps nécessaires :", nombre_swaps)
#print("Sequence de swaps :", sequence_swaps)
#print(len(shortest_path))
