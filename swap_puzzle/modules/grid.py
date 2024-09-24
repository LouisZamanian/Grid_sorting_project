"""
This is the grid module. It contains the Grid class and its associated methods.
"""
#test
import random
from swap_puzzle.modules.graph import Graph
from collections import deque
import copy
import matplotlib.pyplot as plt
import heapq
import sys


#sort utilisé dans l'algorithme a_star lorsque l'on n'utilise pas le module heapq
def sort(L):
    elt=L[-1]
    dist=elt.manhattan_distance()
    for i in range(len(L)-1):
        if L[i].manhattan_distance()>dist:
            L[i],L[-1]=L[-1],L[i]
            break
    return L

class Grid():
    """
    A class representing the grid from the swap puzzle. It supports rectangular grids. 

    Attributes: 
    -----------
    m: int
        Number of lines in the grid
    n: int
        Number of columns in the grid
    state: list[list[int]]
        The state of the grid, a list of list such that state[i][j] is the number in the cell (i, j), i.e., in the i-th line and j-th column. 
        Note: lines are numbered 0..m and columns are numbered 0..n.
    """
    
    def __init__(self, m, n, initial_state = []):
        """
        Initializes the grid.

        Parameters: 
        -----------
        m: int
            Number of lines in the grid
        n: int
            Number of columns in the grid
        initial_state: list[list[int]]
            The intiail state of the grid. Default is empty (then the grid is created sorted).
        """
        self.m = m
        self.n = n
        if not initial_state:
            initial_state = [list(range(i*n+1, (i+1)*n+1)) for i in range(m)]            
        self.state = initial_state



    def __str__(self): 
        """
        Prints the state of the grid as text.
        """
        output = f"The grid is in the following state:\n"
        for i in range(self.m): 
            output += f"{self.state[i]}\n"
        return output

    def __lt__(self, other):
        return self.heuristique() < other.heuristique()
    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

#représentation graphique dans la console python
    def representation_old(self):
        ligne_superieure = "+-------" * (self.n) + "+\n"

        # Lignes du milieu
        lignes_milieu = ""
        for i in range(self.m):
            lignes_milieu += "|"
            for j in range(self.n):
                lignes_milieu += str(self.state[i][j]).center(7)
                if j < self.n - 1:
                    lignes_milieu += "|"
            lignes_milieu += "|\n" + "+-------" * (self.n) + "+\n"

        texte = ligne_superieure + lignes_milieu
        print(texte)

    def create_sorted_grid(self,m, n):
        return [list(range(i * self.n + 1, (i + 1) * self.n + 1)) for i in range(self.m)]

    def trouver_indice_element(self,liste_de_listes, element):
        for i, sous_liste in enumerate(liste_de_listes):
            if element in sous_liste:
                j = sous_liste.index(element)
                return [i, j]  # Retourne le tuple (indice_de_liste, indice_d'élément)
        return None

#question n°2:
    def is_sorted(self):
        """
        Checks if the current state of the grid is sorte and returns the answer as a boolean.
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        for i in range(self.m):
            for j in range(self.n):
                if (i<self.m-1 and self.state[i][self.n-1] > self.state[i + 1][0]) or (j < self.n - 1 and self.state[i][j] > self.state[i][j + 1]):
                    return False
        return True

    def creer_matrice(self,m,n):
        return [[i+j*self.n+1 for i in range(self.n)]for j in range(self.m)]

    def swap(self, cell1, cell2):
        i1,j1=cell1
        i2,j2=cell2
        self.state[i1][j1], self.state[i2][j2] = self.state[i2][j2], self.state[i1][j1]

    def swap_seq(self, cell_pair_list):
        for cell1, cell2 in cell_pair_list:
            self.swap(cell1, cell2)
    @classmethod
    def grid_from_file(cls, file_name):
        with open(file_name, "r") as file:
            m, n = map(int, file.readline().split())
            initial_state = [[] for i_line in range(m)]
            for i_line in range(m):
                line_state = list(map(int, file.readline().split()))
                if len(line_state) != n: 
                    raise Exception("Format incorrect")
                initial_state[i_line] = line_state
            grid = Grid(m, n, initial_state)
        return grid

        # Question n°4
    def representation(self):
        if not self.state or len(self.state) != self.m or any(len(row) != self.n for row in self.state):
            print("La grille n'est pas correctement définie.")
            return

        fig, ax = plt.subplots()
        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.m)

        ax.set_xticks(range(self.n + 1))
        ax.set_yticks(range(self.m))
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.grid(True, which='major', linestyle='-', linewidth=2, color='black')

        for i in range(self.m):
            for j in range(self.n):
                if 0 <= i < self.m and 0 <= j < self.n:
                    ax.text(j + 0.5, self.m - i - 0.5, str(self.state[i][j]), fontsize=12)

        plt.show()


#Question n°6:
#transformation des sommets (matrices) en objets hashable
    def transform(self):
        return tuple(tuple(self.state[i][j] for j in range(self.n) for i in range(self.m)))


#Question n°7:
    #Création du graphe entier, le plus grand possible
    def generate_all_grid_states(self):
        g=Graph()
        queue = deque([self])
        visited = {self.transform()} 

        while queue:
            current_grid = queue.popleft()

            for i in range(self.m):
                for j in range(self.n - 1):
                    # Créer une copie de la grille actuelle pour éviter de la modifier directement
                    new_grid =copy.deepcopy(current_grid)
                    # Échanger les éléments adjacents sur la ligne
                    new_grid.swap((i, j), (i, j+1))
                    new_grid_transform=new_grid.transform()
                    

                    # Vérifier si le nouvel état a déjà été visité
                    if new_grid_transform not in visited:
                        visited.add(new_grid_transform)
                        queue.append(new_grid)
                        g.add_edge(current_grid.transform(), new_grid_transform)

            for i in range(self.m - 1):
                for j in range(self.n):
                    # Créer une copie de la grille actuelle
                    new_grid =copy.deepcopy(current_grid)
                    # Échanger les éléments adjacents sur la colonne
                    new_grid.swap((i, j), (i+1, j))
                    new_grid_transform=new_grid.transform()

                    # Vérifier si le nouvel état a déjà été visité
                    if new_grid_transform not in visited:
                        visited.add(new_grid_transform)
                        queue.append(new_grid)
                        g.add_edge(current_grid.transform(), new_grid_transform)

        return g, g.nb_edges, g.nb_nodes



#Question n°8:
    def next_neighbors_new(self):
        g = Graph()
        queue = deque([self])
        visited = {self.transform()}  # Utilisation d'un ensemble pour stocker les états visités

        while queue:
            current_grid = queue.popleft()

            for i in range(self.m):
                for j in range(self.n - 1):
                    neighbor_grid = copy.deepcopy(current_grid)
                    neighbor_grid.swap((i, j), (i, j + 1))
                    neighbor_transform = neighbor_grid.transform()

                    if neighbor_transform not in visited:
                        visited.add(neighbor_transform)
                        queue.append(neighbor_grid)

                    g.add_edge(current_grid.transform(), neighbor_transform)

                    if neighbor_grid.is_sorted():
                        return g, g.nb_edges, g.nb_nodes

            for i in range(self.m - 1):
                for j in range(self.n):
                    neighbor_grid = copy.deepcopy(current_grid)
                    neighbor_grid.swap((i, j), (i + 1, j))
                    neighbor_transform = neighbor_grid.transform()

                    if neighbor_transform not in visited:
                        visited.add(neighbor_transform)
                        queue.append(neighbor_grid)

                    g.add_edge(current_grid.transform(), neighbor_transform)

                    if neighbor_grid.is_sorted():
                        return g, g.nb_edges, g.nb_nodes

        return g, g.nb_edges, g.nb_nodes


#Séance 3 : Question n°1:
    def distance(self):
        compt=0
        M=self.creer_matrice(self.m,self.n)
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j]!=M[i][j]:
                    compt+=1
        return compt


    def heuristique_old(self):
        compt=0
        L=self.creer_matrice(self.m,self.n)
        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j]!=L[i][j]:
                    compt+=1
        return compt


    def heuristique(self):
        s = 0
        L = self.creer_matrice(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                target_row, target_col = divmod(self.state[i][j] - 1, self.n) #convertir la valeur de la tuile actuelle (self.state[i][j]) en coordonnées de la position cible (target_row, target_col)
                s += abs(i - target_row) + abs(j - target_col)

        return s


    def a_star_final(self):
        g = Graph()
        queue = deque([self])  # Initialiser une deque avec un élément
        visited = {self.transform()}  # Utilisation d'un ensemble pour stocker les états visités

        while queue:
            current_grid = queue.popleft()  # Utiliser popleft sur une deque

            for i in range(self.m):
                for j in range(self.n):
                    if i < self.m - 1:
                        neighbor_grid_1 = copy.deepcopy(current_grid)
                        neighbor_grid_1.swap((i, j), (i + 1, j))
                        neighbor_transform_1 = neighbor_grid_1.transform()

                        if neighbor_transform_1 not in visited:
                            visited.add(neighbor_transform_1)
                            queue.append(neighbor_grid_1)
                            queue=sort(queue)
                        g.add_edge(current_grid.transform(), neighbor_transform_1)

                        if neighbor_grid_1.is_sorted():
                            return g, g.nb_edges, g.nb_nodes

                    if j < self.n - 1:
                        neighbor_grid_2 = copy.deepcopy(current_grid)
                        neighbor_grid_2.swap((i, j), (i, j + 1))
                        neighbor_transform_2 = neighbor_grid_2.transform()

                        if neighbor_transform_2 not in visited:
                            visited.add(neighbor_transform_2)
                            queue.append(neighbor_grid_2)
                            queue=sort(queue)
                        g.add_edge(current_grid.transform(), neighbor_transform_2)

                        if neighbor_grid_2.is_sorted():
                            return g, g.nb_edges, g.nb_nodes

        return g, g.nb_edges, g.nb_nodes

    def a_star_final_heapq(self):
        g = Graph()
        initial_state = (self.heuristique(), self)
        queue = [initial_state]  # Utiliser une liste pour le tas
        visited = {self.transform()}

        while queue:
            _, current_grid = heapq.heappop(queue)

            for i in range(self.m):
                for j in range(self.n):
                    if i < self.m - 1:
                        neighbor_grid_1 = copy.deepcopy(current_grid)
                        neighbor_grid_1.swap((i, j), (i + 1, j))
                        neighbor_transform_1 = neighbor_grid_1.transform()

                        if neighbor_transform_1 not in visited:
                            visited.add(neighbor_transform_1)
                            heapq.heappush(queue, (neighbor_grid_1.heuristique(), neighbor_grid_1))
                        g.add_edge(current_grid.transform(), neighbor_transform_1)

                        if neighbor_grid_1.is_sorted():
                            return g, g.nb_edges, g.nb_nodes

                    if j < self.n - 1:
                        neighbor_grid_2 = copy.deepcopy(current_grid)
                        neighbor_grid_2.swap((i, j), (i, j + 1))
                        neighbor_transform_2 = neighbor_grid_2.transform()

                        if neighbor_transform_2 not in visited:
                            visited.add(neighbor_transform_2)
                            heapq.heappush(queue, (neighbor_grid_2.heuristique(), neighbor_grid_2))
                        g.add_edge(current_grid.transform(), neighbor_transform_2)

                        if neighbor_grid_2.is_sorted():
                            return g, g.nb_edges, g.nb_nodes

        return g, g.nb_edges, g.nb_nodes


#test de la représentation graphique
grid=Grid(2,4,[[4,2,3,1],[5,6,7,8]])
grid.representation()










                

        





