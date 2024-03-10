from grid import Grid


class Solver(Grid):
    def __init__(self, m, n, initial_state=None):
        super().__init__(m, n, initial_state)
        self.n = n
        self.m = m

    def creer_matrice(self,m,n):
        return [[i+j*self.n+1 for i in range(self.n)]for j in range(self.m)]


#Solution naïve
    def get_solution(self):
        swp = []
        nb = 0
        Lo = self.creer_matrice(self.m, self.n)
        while self.state != Lo:
            for i in range(1, self.n * self.m + 1):
                x = self.trouver_indice_element(Lo, i)
                ind = self.trouver_indice_element(self.state, i)
                while ind[0] != x[0]:
                    if x[0] < ind[0]:
                        self.swap((ind[0] - 1, ind[1]), (ind[0], ind[1]))
                        swp.append(((ind[0] - 1, ind[1]), (ind[0], ind[1])))
                        ind[0] -= 1
                    elif x[0] > ind[0]:
                        self.swap((ind[0] + 1, ind[1]), (ind[0], ind[1]))
                        swp.append(((ind[0] + 1, ind[1]), (ind[0], ind[1])))
                        ind[0] += 1
                    nb += 1
                while ind[1] != x[1]:
                    if x[1] < ind[1]:
                        self.swap((ind[0], ind[1] - 1), (ind[0], ind[1]))
                        swp.append(((ind[0], ind[1] - 1), (ind[0], ind[1])))
                        ind[1] -= 1
                    elif x[1] > ind[1]:
                        self.swap((ind[0], ind[1] + 1), (ind[0], ind[1]))
                        swp.append(((ind[0], ind[1] + 1), (ind[0], ind[1])))
                        ind[1] += 1
                    nb += 1

        return nb, swp

#Test de la fonction
grid1= Solver(2, 3, [[1, 3,4], [2, 6,5]])
grid2=Solver(2,2,[[1,3],[4,2]])
print(grid2.get_solution())