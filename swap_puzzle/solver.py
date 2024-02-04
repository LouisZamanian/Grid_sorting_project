from grid import Grid

def trouver_indice_element(liste_de_listes, element):
    for i, sous_liste in enumerate(liste_de_listes):
        if element in sous_liste:
            j = sous_liste.index(element)
            return [i, j]  # Retourne le tuple (indice_de_liste, indice_d'élément)
    return None

def creer_matrice(n,m):
    return [[i+j*m+1 for i in range(m)]for j in range(n)]


class Solver(Grid):
    def __init__(self, n, m):
        # Call the constructor of the parent class (Grid)
        super().__init__(n, m)
        self.n = n
        self.m = m

    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        # TODO: implement this function (and remove the line "raise NotImplementedError").
        # NOTE: you can add other methods and subclasses as much as necessary. The only thing imposed is the format of the solution returned.
        swp = []
        nb = 0
        Lo = self.creer_matrice(self.n, self.m)  # Use self to access the class attribute
        while self.state != Lo:
            for i in range(1, self.n * self.m + 1):
                x = self.trouver_indice_element(Lo, i)  # Use self to access the method
                for k in range(self.n):
                    for j in range(self.m):
                        if self.state[k][j] == i:
                            ind = [k, j]
                while ind != x:
                    nb += 1
                    if x[0] < ind[0]:
                        self.swap(self.state, (ind[0] - 1, ind[1]), (ind[0], ind[1]))
                        swp.append((self.state[ind[0] - 1][ind[1]], self.state[ind[0]][ind[1]]))
                        ind[0] -= 1
                        
                    elif x[0] > ind[0]:
                        self.swap(self.state, (ind[0] + 1, ind[1]), (ind[0], ind[1]))
                        swp.append((self.state[ind[0] + 1][ind[1]], self.state[ind[0]][ind[1]]))
                        ind[0] += 1
                        
                    if x[1] < ind[1]:
                        self.swap(self.state, (ind[0], ind[1] - 1), (ind[0], ind[1]))
                        swp.append((self.state[ind[0]][ind[1] - 1], self.state[ind[0]][ind[1]]))
                        ind[1] -= 1
                        
                    elif x[1] > ind[1]:
                        self.swap(self.state, (ind[0] + 1, ind[1]), (ind[0], ind[1]))
                        swp.append((self.state[ind[0] + 1][ind[1]], self.state[ind[0]][ind[1]]))
                        ind[1] += 1
                        
        return nb, swp