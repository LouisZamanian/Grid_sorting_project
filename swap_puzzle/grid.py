"""
This is the grid module. It contains the Grid class and its associated methods.
"""
#test
import random
from graph import Graph
from collections import deque
import copy
import matplotlib.pyplot as plt
import heapq
import sys


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
        # Implémentez la logique de comparaison nécessaire
        return self.heuristique() < other.heuristique()
    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    def representation(self):
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
        """
        Implements the swap operation between two cells. Raises an exception if the swap is not allowed.

        Parameters: 
        -----------
        cell1, cell2: tuple[int]
            The two cells to swap. They must be in the format (i, j) where i is the line and j the column number of the cell. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        i1,j1=cell1
        i2,j2=cell2
        self.state[i1][j1], self.state[i2][j2] = self.state[i2][j2], self.state[i1][j1]

    def swap_seq(self, cell_pair_list):
        """
        Executes a sequence of swaps. 

        Parameters: 
        -----------
        cell_pair_list: list[tuple[tuple[int]]]
            List of swaps, each swap being a tuple of two cells (each cell being a tuple of integers). 
            So the format should be [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...].
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        for cell1, cell2 in cell_pair_list:
            self.swap(cell1, cell2)
    @classmethod
    def grid_from_file(cls, file_name): 
        """
        Creates a grid object from class Grid, initialized with the information from the file file_name.
        
        Parameters: 
        -----------
        file_name: str
            Name of the file to load. The file must be of the format: 
            - first line contains "m n" 
            - next m lines contain n integers that represent the state of the corresponding cell

        Output: 
        -------
        grid: Grid
            The grid
        """
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



    def transform(self):
        return tuple(tuple(self.state[i][j] for j in range(self.n) for i in range(self.m)))





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

        return visited,len(visited)


    def representation(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.n)  #on créer les axes verticaux et horizontaux à la bonne taille
        ax.set_ylim(0, self.m)

        ax.set_xticks(range(self.m+1))
        ax.set_yticks(range(self.n))
        ax.set_xticklabels([]) #on supprime les graduations pour ne garder que la grille
        ax.set_yticklabels([])
        ax.grid(True, which='major', linestyle='-', linewidth=2, color='black') #on trace le cadrillage
        for i in range(self.m):
            for j in range(self.n):
                ax.text(j+0.5,self.m-i-0.5, str(self.state[i][j]), fontsize=12) #on remplit la grille 
        plt.show()






 #   def next_neighbors(self):
  #      g = Graph()
   #     compt=0
    #    queue = deque([Grid(self.m, self.n, self.state)])
     #   cond=False
      #  arretes=0
       # noeuds=1
  # Ajoutez la grille initiale à la file d'attente
        
        #while cond==False:
         #   compt+=1
          #  print(compt)
           # current_grid=queue.popleft()
            
            # Parcourir les lignes
            
            #for i in range(self.n):
             #   for j in range(self.m - 1):
                    # Créer une copie de la grille actuelle pour éviter de la modifier directement
              #      neighbor_grid = copy.deepcopy(current_grid)

                    # Échanger les éléments adjacents sur la ligne
               #     neighbor_grid.swap((i, j), (i, j + 1))

                     # Ajouter une arête au graphe
                #    if neighbor_grid.transform() in g.nodes or neighbor_grid.transform() in g.edges:
                 #       noeuds+=1
                  #  g.add_edge(current_grid.transform(),neighbor_grid.transform())
                   # arretes+=1


                    #if neighbor_grid.is_sorted():
                     #   cond=True
                      #  break
                
                    #else:
                    # Ajouter la nouvelle grille à la file d'attente
                     #   queue.append(neighbor_grid)
                #if cond==True:
                 #   break




            # Parcourir les colonnes
            #if cond==False:
             #   for i in range(self.n - 1):
              #      for j in range(self.m):
                    # Créer une copie de la grille actuelle
               #         neighbor_grid = copy.deepcopy(current_grid)

                    # Échanger les éléments adjacents sur la colonne
                #        neighbor_grid.swap((i, j), (i + 1, j))

                     # Ajouter une arête au graphe
                 #       if neighbor_grid.transform() in g.nodes or neighbor_grid.transform() in g.edges:
                  #          noeuds+=1   
                   #     g.add_edge(current_grid.transform(),neighbor_grid.transform())
                    #    arretes+=1

                     #   if neighbor_grid.is_sorted():
                      #      cond=True
                       #     break
                
                        #else:
                    # Ajouter la nouvelle grille à la file d'attente
                         #   queue.append(neighbor_grid)
                #if cond==True:
                 #   break
                    
       # return g,arretes,noeuds


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

    def manhattan_distance(self):
        distance = 0
        for i in range(self.m):
            for j in range(self.n):
                value = self.state[i][j]
                goal_i, goal_j = divmod(value - 1, self.n)
                distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def heuristique(self):
        s = 0
        L = self.creer_matrice(self.m, self.n)

        for i in range(self.m):
            for j in range(self.n):
                if self.state[i][j] != 0:  # Ignorer la case vide s'il y en a une
                    target_row, target_col = divmod(self.state[i][j] - 1, self.n)
                    s += abs(i - target_row) + abs(j - target_col)

        return s




    def a_star(self):
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
                        sort(queue)

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
                        sort(queue)

                    g.add_edge(current_grid.transform(), neighbor_transform)

                    if neighbor_grid.is_sorted():
                        return g, g.nb_edges, g.nb_nodes

        return g, g.nb_edges, g.nb_nodes

    def a_star_new_new(self):
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
                            queue = deque(sorted(queue, key=lambda x: x.heuristique()))
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
                            queue = deque(sorted(queue, key=lambda x: x.heuristique()))
                        g.add_edge(current_grid.transform(), neighbor_transform_2)

                        if neighbor_grid_2.is_sorted():
                            return g, g.nb_edges, g.nb_nodes

        return g, g.nb_edges, g.nb_nodes


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









                

        





