"""
This is the grid module. It contains the Grid class and its associated methods.
"""

import random
from graph import Graph
from collections import deque
import copy

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

    def __repr__(self): 
        """
        Returns a representation of the grid with number of rows and columns.
        """
        return f"<grid.Grid: m={self.m}, n={self.n}>"

    

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

    def creer_matrice(self,n,m):
        return [[i+j*self.m+1 for i in range(self.m)]for j in range(self.n)]

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
    
    def next_neighbors(self):
        g = Graph()
        compt=0
        queue = deque([Grid(self.m, self.n, self.state)])
        cond=False
  # Ajoutez la grille initiale à la file d'attente
        
        while cond==False:
            compt+=1
            print(compt)
            current_grid=queue.popleft()
            
            # Parcourir les lignes
            
            for i in range(self.n):
                for j in range(self.m - 1):
                    # Créer une copie de la grille actuelle pour éviter de la modifier directement
                    neighbor_grid = copy.deepcopy(current_grid)

                    # Échanger les éléments adjacents sur la ligne
                    neighbor_grid.swap((i, j), (i, j + 1))

                     # Ajouter une arête au graphe
                    g.add_edge(current_grid.transform(),neighbor_grid.transform())

                    if neighbor_grid.is_sorted():
                        cond=True
                        break
                
                    else:
                    # Ajouter la nouvelle grille à la file d'attente
                        queue.append(neighbor_grid)
                if cond==True:
                    break




            # Parcourir les colonnes
            if cond==False:
                for i in range(self.n - 1):
                    for j in range(self.m):
                    # Créer une copie de la grille actuelle
                        neighbor_grid = copy.deepcopy(current_grid)

                    # Échanger les éléments adjacents sur la colonne
                        neighbor_grid.swap((i, j), (i + 1, j))

                     # Ajouter une arête au graphe
                        g.add_edge(current_grid.transform(),neighbor_grid.transform())

                        if neighbor_grid.is_sorted():
                            cond=True
                            break
                
                        else:
                    # Ajouter la nouvelle grille à la file d'attente
                            queue.append(neighbor_grid)
                if cond==True:
                    break
        print(neighbor_grid)
                    
        return g




                

        





